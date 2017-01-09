from django import forms
from .models import SignUp
from django.forms import ModelForm, Textarea

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = '__all__'

		