import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csms_web.settings')

app = Celery('csms_web')

# In case when timezone is not 'UTC', celery timezone should be updated explicitly:
# app.conf.enable_utc = False
# app.conf.update(timezone='django.conf:settings.CELERY_TIMEZONE')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
