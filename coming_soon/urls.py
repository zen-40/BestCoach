from django.urls import path
from . import views


app_name='coming_soon'


urlpatterns = [
    path('', views.home, name='home'),
]