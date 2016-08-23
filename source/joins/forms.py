from django import forms
from .models import Join

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join

class EmailForm(forms.Form):
	email = forms.EmailField()