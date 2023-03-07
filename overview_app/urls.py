from django.urls import path
from . import views


app_name = 'overview_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('functions/', views.functions, name='functions'),
    path('vote-for-news/', views.vote_for_news, name='vote_for_news'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]