from django import forms

class MyForms(forms.Form):
	message = forms.CharField(max_length=80, required = True, label='Message')