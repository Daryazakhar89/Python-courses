from pyexpat import model
from .models import MySite
from django.forms import ModelForm, TextInput, Textarea

class MySiteForms(ModelForm):
    class Meta:
        model = MySite
        fields = ['title', 'content']
        