from django.urls import  path
from . import views

urlpatterns = [
    path('users', views.user_all),
    path('users/<int:pk>', views.user_id),
    path('tasks', views.task_all),
    path('tasks/<int:pk>', views.task_id),
]