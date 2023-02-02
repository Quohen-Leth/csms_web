from django.urls import path

from .views import TryRunTaskView

urlpatterns = [
    path("runtask/", TryRunTaskView.as_view(), name="try_task")
]
