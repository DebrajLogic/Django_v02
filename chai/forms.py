from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label='Select Chai Variety')
    