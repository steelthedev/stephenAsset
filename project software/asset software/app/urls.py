from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('dashboard/', views.Dashboard, name="dashboard"),
    path('asset/', views.Asset, name="asset"),
    path('staffs/', views.Staffs, name="staffs"),
    path('addAsset/', views.AddAsset, name="addAsset"),
]
