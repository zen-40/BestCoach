from django.shortcuts import render
from .models import BodyProgress, Meal


def home(request):
    template_name = 'Home'

    context = {'template_name': template_name,}
    return render(request, 'app/home.html', context)



def body_progress(request):
    template_name = 'Body progress'
    query = BodyProgress.objects.all()

    context = {'query': query,
               'template_name': template_name}
    return render(request, 'app/body_progress.html', context)



def diet(request):
    template_name = 'Diet plan'
    query = Meal.objects.all()

    context = {'query': query,
               'template_name': template_name}
    return render(request, 'app/diet.html', context)



def training(request):
    template_name = 'Training plan'

    context = {'template_name': template_name}
    return render(request, 'app/training.html', context)



def chat_coach(request):
    template_name = 'Chat with a personal trainer'

    context = {'template_name': template_name}
    return render(request, 'app/chat_coach.html', context)



def settings_general(request):
    template_name = 'Settings general'
    activation_tab = 1

    context = {'activation_tab': activation_tab,
               'template_name': template_name}
    return render(request, 'app/settings_general.html', context)


def settings_billing(request):
    template_name = 'Settings billing'
    activation_tab = 2

    context = {'activation_tab': activation_tab,
               'template_name': template_name}
    return render(request, 'app/settings_billing.html', context)



def settings_security(request):
    template_name = 'Settings security'
    activation_tab = 3

    context = {'activation_tab': activation_tab,
               'template_name': template_name,}
    return render(request, 'app/settings_security.html', context)


def settings_notifications(request):
    template_name = 'Settings notifications'
    activation_tab = 4

    context = {'activation_tab': activation_tab,
               'template_name': template_name}
    return render(request, 'app/settings_notifications.html', context)

