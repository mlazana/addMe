from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Add_Form(forms.Form):
	username = forms.CharField(label='username', max_length=100)

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()


	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']