from django import forms
from .models import *


class SubscribeForms(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]


