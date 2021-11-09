from django import forms
from django.forms import ModelForm

from .models import Tournament


class DateInput(forms.DateInput):
    input_type = 'date'


class TournamentForm(ModelForm):

    class Meta:
        model = Tournament
        fields = ['start_time']
        widgets = {
            'start_time': DateInput(),
        }