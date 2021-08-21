from django import forms
from django.forms import fields
from .models import Decade, Fad

class DecadeForm(forms.ModelForm):
    class Meta:
        model = Decade
        fields = ('start_year',) # trailing comma for tuple instead of str

class FadForm(forms.ModelForm):
    class Meta:
        model = Fad
        fields = ('name', 'image_url', 'description')