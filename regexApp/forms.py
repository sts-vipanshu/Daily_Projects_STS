from regexApp.models import *
from django.forms import ModelForm

class regexPatternForm(ModelForm):
    class Meta:
        model=regexPattern
        fields="__all__"
    