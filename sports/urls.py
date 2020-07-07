from django.urls import path
from . import views

app_name='sports'
urlpatterns = [
    path('', views.main3, name="main3"),
    path('airmax/', views.airmax, name="airmax"),
    path('jordan/', views.jordan, name="jordan"),
]