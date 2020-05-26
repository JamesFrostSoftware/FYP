from django import forms

class MovieSearchForm(forms.Form):
	post = forms.TextInput()