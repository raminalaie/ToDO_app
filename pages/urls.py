from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("create/", views.TaskCreate.as_view(), name="create_task"),
]