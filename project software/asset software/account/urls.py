from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login, name='login'),
    path('createStaff/', views.CreateStaff, name="createStaff"),
]
