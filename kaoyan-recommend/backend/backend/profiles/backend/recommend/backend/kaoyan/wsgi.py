python<br>import os<br>from django.core.wsgi import get_wsgi_application<br><br>os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kaoyan.settings')<br>application = get_wsgi_application()<br>
