import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from profiles.models import StudentProfile
from universities.models import University, Admission
from .engine import RuleRecommendEngine

logger = logging.getLogger('recommend')

@api_view(['POST'])
def recommend(request):
    profile_id = request.data.get('profile_id')
    if not profile_id:
        return Response({'code': 'PROFILE_REQUIRED', 'message': '缺少 profile_id'}, status=400)
    profile = get_object_or_404(StudentProfile, pk=profile_id)

    candidates = []
    for uni in University.objects.all():
        for major in uni.majors.all():
            admission = Admission.objects.filter(major=major, year=2025).first()
            if admission:
                candidates.append((uni, major, admission))

    try:
        engine = RuleRecommendEngine()
        results = engine.recommend(profile, candidates)
        logger.info(f"profile_id={profile_id}, candidates={len(results)}")
        return Response({
            'ai_enabled': False,
            'degraded': True,
            'notice': 'AI服务暂不可用，已回退为规则推荐（非AI基础推荐）',
            'candidates': results,
        })
    except Exception as e:
        logger.error(f"recommend error: {e}")
        return Response({'code': 'RECOMMEND_ERROR', 'message': str(e)}, status=500)