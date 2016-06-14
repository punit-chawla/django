import re
from django import forms
from django.utils.translation import ugettext_lazy as _
class addteacherform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'max_length': 30}),label=_("Teacher Name"))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'max_length': 30}),label=_("Qualification"))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'required': True, 'max_length': 30}), label=_("Address"))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'max_length': 30}),label=_("City"))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'max_length': 30}),label=_("State"))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'max_length': 30}),label=_("Phone Number"))
    expeirience = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'max_length': 30}),label=_("Experience"))

