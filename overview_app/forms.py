from django import forms
from .models import Contact, ContactAdvanced
from django.forms import Textarea



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {'name', 'phone', 'data'}


class ContactAdvancedForms(forms.ModelForm):
    class Meta:
        model = ContactAdvanced
        fields = {'name', 'surname', 'email', 'contact'}
        widgets = {'contact': Textarea(attrs={'rows': '6',
                                              'class': 'form-control',
                                              'placeholder': 'Write the content of the message sent to our team...'})}