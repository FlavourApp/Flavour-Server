from django import forms
from db.models import *

class ReservaForm(forms.ModelForm):
  class Meta:
  	model = Reserva

class ComunaForm(forms.Form):
	comuna = forms.ModelChoiceField(queryset=Comuna.objects.all())