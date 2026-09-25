from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import University
from .serializers import UniversitySerializer

@api_view(['GET'])
def list_universities(request):
    qs = University.objects.all()
    region = request.query_params.get('region')
    level = request.query_params.get('level')
    if region:
        qs = qs.filter(region=region)
    if level:
        qs = qs.filter(level=level)
    return Response(UniversitySerializer(qs, many=True).data)