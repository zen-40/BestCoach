from django.shortcuts import render
from .models import SimpleCms



def home(request):
    cms = SimpleCms.objects.last()

    context = {'cms': cms}
    return render(request, 'overview_app/home.html', context)