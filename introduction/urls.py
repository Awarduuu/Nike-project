from django.urls import path
from . import views

app_name='introduction'
urlpatterns = [
    path('', views.main, name="main"),
    path('nikeXsacai/', views.sacai, name="sacai"),
    path('nikeXsupreme/', views.supreme, name="supreme"),
    path('nikeXstussy/', views.stussy, name="stussy"),
]