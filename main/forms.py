# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django.forms.extras.widgets import *

from main.models import Negocio

# forms
class FormProposta(ModelForm):
    class Meta:
        model = Negocio
        exclude = ['criado', 'atualizado',]
        

