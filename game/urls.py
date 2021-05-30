from django.urls import path
from . import views

app_name = 'csg'

urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name='signup'),
    path('how/', views.HowView.as_view(), name="how"),
    path('download/', views.download, name="download"),
    path('download/windows', views.zip_file_view_windows, name="windows"),
    path('download/mac', views.zip_file_view_mac, name="mac"),
    path('support/', views.support, name='support'),
    path('reflection/', views.reflection, name='reflection'),
]