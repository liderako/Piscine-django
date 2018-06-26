from django import forms

class removeForm(forms.Form):
	name = forms.CharField(max_length=256, required = True, label='Update')