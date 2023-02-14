from django.shortcuts import render
from .models import BodyProgress, Meal


def home(request):
    return render(request, 'app/home.html')



def body_progress(request):
    query = BodyProgress.objects.all()

    context = {'query': query}
    return render(request, 'app/body_progress.html', context)



def diet(request):
    query = Meal.objects.all()

    context = {'query': query}
    return render(request, 'app/diet.html', context)



def training(request):
    return render(request, 'app/training.html')



def chat_coach(request):
    return render(request, 'app/chat_coach.html')



def settings_general(request):
    activation_tab = 1

    context = {'activation_tab': activation_tab}
    return render(request, 'app/settings_general.html', context)


def settings_billing(request):
    activation_tab = 2

    context = {'activation_tab': activation_tab}
    return render(request, 'app/settings_billing.html', context)



def settings_security(request):
    activation_tab = 3

    context = {'activation_tab': activation_tab}
    return render(request, 'app/settings_security.html', context)


def settings_notifications(request):
    activation_tab = 4

    context = {'activation_tab': activation_tab}
    return render(request, 'app/settings_notifications.html', context)

