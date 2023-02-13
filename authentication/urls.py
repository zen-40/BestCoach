from django.urls import path
from .views import LogIn, SignUp


app_name = 'authentication'


urlpatterns = [
    path('', LogIn.as_view(), name='login'),
    path('sign-up/', SignUp.as_view(), name='signup'),
]