from pyexpat import model
from .models import MySite
from django.forms import ModelForm, TextInput, Textarea

class MySiteForms(ModelForm):
    class Meta:
        model = MySite
        fields = ['title', 'content']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name and email ',
            }),
            "content": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your request ',
            }),
        }