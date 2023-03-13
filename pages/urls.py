from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("create/", views.TaskCreate.as_view(), name="create_task"),
    path("status/<int:pk>/", views.TaskComplete.as_view(), name="status_change"),
    path("update/<int:pk>/", views.TaskUpdate.as_view(), name="update_task"),
    path("/<int:pk>/delete/", views.PostDelete.as_view(), name="DeleteView"),
]