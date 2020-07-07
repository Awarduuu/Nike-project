from django.urls import path
from . import views

app_name='lifestyle'
urlpatterns = [
    path('', views.main2, name="main2"),
    path('daybreak/', views.daybreak, name="daybreak"),
    path('blazer/', views.blazer, name="blazer"),
]