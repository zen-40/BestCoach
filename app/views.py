from django.shortcuts import render
from .models import BodyProgress


def home(request):
    return render(request, 'app/home.html')



def body_progress(request):
    query = BodyProgress.objects.all()

    context = {'query': query}
    return render(request, 'app/body_progress.html', context)



def diet(request):
    return render(request, 'app/diet.html')



def training(request):
    return render(request, 'app/training.html')



def chat_coach(request):
    return render(request, 'app/chat_coach.html')



def notifications(request):
    return render(request, 'app/notifications.html')



def settings_and_payment(request):
    return render(request, 'app/settings_and_payment.html')
