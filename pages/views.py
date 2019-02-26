from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .addForm import RegisterForm,Add_Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
from .models import User_account




def index(request):
	return render(request, "index.html",{})

def contact(request):
	return render(request, "contact.html",{})

def add(request):
	if request.method == "POST":
		form = Add_Form(request.POST)
		if form.is_valid():
			text = form.cleaned_data['username']
			usr = User.objects.get(username=text)
			uid = usr.id
			u = User_account.objects.get(user_id=uid)
			return render(request, 'add.html', {"users": u})
		else:
			return redirect('add/')
	else:
		form = Add_Form()
	return render(request, 'add.html', {'form': form})
	
def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login.')
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form})

def login(request):
	return render(request, "login.html",{})

def logout(request):
	return render(request, "logout.html",{})

@login_required
def profile(request):
	return render(request, 'users/profile.html')

