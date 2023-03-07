from django.urls import path
from . import  views


app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('body-progress/', views.body_progress, name='body_progress'),
    path('diet/', views.diet, name='diet'),
    path('training/', views.training, name='training'),
    path('chat-coach/', views.chat_coach, name='chat_coach'),
    #settigs
    path('settings/general/', views.settings_general, name='settings_general'),
    path('settings/billing/', views.settings_billing, name='settings_billing'),
    path('settings/security/', views.settings_security, name='settings_security'),
    path('settings/notifications/', views.settings_notifications, name='settings_notifications'),
    path('sample/', views.sample, name='sample'),
]


