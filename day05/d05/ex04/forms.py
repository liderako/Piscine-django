from django import forms

class removeForm(forms.Form):
	title = forms.CharField(max_length=256, required = True, label='Remove')