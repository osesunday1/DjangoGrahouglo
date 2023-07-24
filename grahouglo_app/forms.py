from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *

#CREATE Feedback Form

class ClientFeedbackForm(ModelForm):
    email= forms.EmailInput()
    number= forms.TextInput() 
    name = forms.TextInput()
    message = forms.TextInput()
    class Meta: 
        model = ClientFeedback
        fields= ('email', 'number', 'name', 'message')

        widgets= {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': "Your Email"}),
            'number': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Your Number"}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Full Name"}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder': "Brief us on what you need"}),
        }

        labels= {
            'name': '',
            'number': '',
            'email': '',
            'message': '',
        }

         
    
