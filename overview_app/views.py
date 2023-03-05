from django.shortcuts import render
from .forms import ContactForm, ContactAdvancedForms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article, TermsAndConditions



def home(request):
    send = request.session.get('send')
    if send:
        request.session['send'] = None

    #contact form
    if request.method == 'POST' and 'buttonSend' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['send'] = 'Thank you, the form has been completed correctly. Wait for our employee to contact you.'
            return HttpResponseRedirect(reverse('overview_app:home'))
    else:
        form = ContactForm()

    context = {'send': send,
               'form': form}
    return render(request, 'overview_app/home.html', context)



def contact(request):
    #contact form
    if request.method == 'POST' and 'buttonSend' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['send'] = 'Thank you, the form has been completed correctly. Wait for our employee to contact you.'
            return HttpResponseRedirect(reverse('overview_app:home'))
    else:
        form = ContactForm()

    contact_form = ContactAdvancedForms()

    context = {'form': form,
               'contact_form': contact_form}
    return render(request, 'overview_app/contact.html', context)



def functions(request):
    #functions
    obj = Article.objects.last()

    #contact form
    if request.method == 'POST' and 'buttonSend' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['send'] = 'Thank you, the form has been completed correctly. Wait for our employee to contact you.'
            return HttpResponseRedirect(reverse('overview_app:home'))
    else:
        form = ContactForm()

    context = {'form': form,
               'obj': obj}
    return render(request, 'overview_app/functions.html', context)



def vote_for_news(request):
    #contact form
    if request.method == 'POST' and 'buttonSend' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['send'] = 'Thank you, the form has been completed correctly. Wait for our employee to contact you.'
            return HttpResponseRedirect(reverse('overview_app:home'))
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'overview_app/vote_for_news.html', context)



def terms(request):
    #specific
    obj = TermsAndConditions.objects.last()

    #contact form
    if request.method == 'POST' and 'buttonSend' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['send'] = 'Thank you, the form has been completed correctly. Wait for our employee to contact you.'
            return HttpResponseRedirect(reverse('overview_app:home'))
    else:
        form = ContactForm()

    context = {'form': form,
               'obj': obj}
    return render(request, 'overview_app/terms.html', context)



def privacy(request):
    #specific
    obj = TermsAndConditions.objects.last()

    #contact form
    if request.method == 'POST' and 'buttonSend' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['send'] = 'Thank you, the form has been completed correctly. Wait for our employee to contact you.'
            return HttpResponseRedirect(reverse('overview_app:home'))
    else:
        form = ContactForm()

    context = {'form': form,
               'obj': obj}
    return render(request, 'overview_app/privacy.html', context)