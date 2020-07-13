from django.urls import path 
from .views import Taskslist

urlpatterns = [
    path('tasklist/', Taskslist.as_view())
]
