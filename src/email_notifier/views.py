import logging
import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .tasks import run_once_task, schedule_task

logger = logging.getLogger(__name__)


class TryRunTaskView(APIView):
    """Test view  to check celery tasks."""
    def get(self, request, *args, **kwargs):
        logger.info("Task test view")
        # run_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
        # run_once_task.apply_async(eta=run_time)
        schedule_task()
        return Response(status=status.HTTP_202_ACCEPTED)
