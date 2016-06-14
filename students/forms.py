import re
from django import forms
from django.utils.translation import ugettext_lazy as _
class addstudentform (forms.Form):
	 name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','required':True,'max_length':30}), label=_("Name"))
	 classs=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','required':True,'max_length':30}), label=_("Class"))
	
	 #user_id = forms.IntegerField(widget=forms.HiddenInput)