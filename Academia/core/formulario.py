from django.test import TestCase

from django import forms
from .models import Assinar
# Create your tests here.

class TreinaForm(forms.ModelForm):
    class Meta:
        model = Assinar
        fields = ['Nome','Treino','Quant','Cpf','Preco']
