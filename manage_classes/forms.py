import re
from django import forms
from django.utils.translation import ugettext_lazy as _
class addclassform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'max_length': 30}),label=_("Class Name"))
    

