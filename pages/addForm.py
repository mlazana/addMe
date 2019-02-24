from django import forms

class Add_Form(forms.Form):
	username = forms.CharField(label='username', max_length=100)