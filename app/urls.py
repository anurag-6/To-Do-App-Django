from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name = 'home'),
    path('add_task/',add_task,name = 'add'),
    path('delete/<tid>/',del_task,name='del'),
    path('edit/<tid>/',edit_task,name='edit'),
    path('complete/<tid>/',complete,name='do'),
    path('view_completed/',view_completed,name='done'),





]
