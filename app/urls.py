from django.urls import path
from . import  views


app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('body-progress/', views.body_progress, name='body_progress'),
    path('diet/', views.diet, name='diet'),
    path('training/', views.training, name='training'),
    path('chat-coach/', views.chat_coach, name='chat_coach'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings-and-payments/', views.settings_and_payment, name='settings_and_payment'),
]


