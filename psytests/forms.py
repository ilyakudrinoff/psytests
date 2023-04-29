from django import forms
from .models import Psyhologes, Tests


class PsyhologesForm(forms.ModelForm):
    class Meta:
        model = Psyhologes
        fields = ['name', 'phone_number', 'gender', 'old', 'instagram', 'telegram', 'email']
