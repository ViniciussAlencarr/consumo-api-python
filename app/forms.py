from django.db.models import fields
from django.forms import ModelForm
from django import forms
from app.models import *

class ConsultaCepForm(forms.ModelForm):
    class Meta:
        model = ConsultaCep
        fields = '__all__'