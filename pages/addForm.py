from django import forms
from pages.models import Member

class Add_Form(forms.Form):
	username = forms.CharField(label='username', max_length=100)

class RegisterForm(forms.ModelForm):
	fullName = forms.CharField(label='fullName', max_length=200)
	username = forms.CharField(label='username', max_length=200)
	psw = forms.CharField(label='psw', max_length=200)
	email = forms.EmailField(label='email', max_length=254)
	fb_account = forms.CharField(label='fb_account', max_length=200)
	in_account = forms.CharField(label='in_account', max_length=200)
	tw_account = forms.CharField(label='tw_account', max_length=200)
	gt_account = forms.CharField(label='gt_account', max_length=200)

	class Meta:
		model = Member
		fields = ('fullName','username', 'psw', 'email', 'fb_account', 'in_account', 'tw_account', 'gt_account',)