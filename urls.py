from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('todo/', views.todo,name='todo'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]