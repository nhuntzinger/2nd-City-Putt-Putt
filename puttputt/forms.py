from django import forms
from django.forms import ModelForm

from .models import DrinkInfo, Tournament


class DateInput(forms.DateInput):
    input_type = 'date'


class TournamentForm(ModelForm):

    class Meta:
        model = Tournament
        fields = ['start_time']
        widgets = {
            'start_time': DateInput(),
        }

class DrinkForm(forms.Form):
    title = forms.CharField(label='title', max_length=30)
    price = forms.IntegerField(label='price')
    image = forms.CharField(label='image', max_length=500, required=False)
