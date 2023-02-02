import logging
import pytz
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, CrontabSchedule

from csms_web.celery import app as celery_app

logger = logging.getLogger(__name__)


@celery_app.task()
def run_once_task():
    logger.info("This is celery task!!!!!")


@celery_app.task()
def scheduled_task():
    logger.info("This task was scheduled to run once!!!!")


def schedule_task():
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute="1",
        hour="*",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
        timezone=pytz.UTC,
    )

    PeriodicTask.objects.create(
        crontab=schedule,
        one_off=True,
        task="email_notifier.tasks.scheduled_task",
        name="ten_seconds_task",
        # expires=datetime.utcnow() + timedelta(minutes=30),
    )
