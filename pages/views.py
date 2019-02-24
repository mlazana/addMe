from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .addForm import Add_Form, RegisterForm
from .models import Member, Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def index(request):
	return render(request, "index.html",{})

def contact(request):
	return render(request, "contact.html",{})

def add(request):
	if (request.method == 'POST'): 
		form = Add_Form(request.POST)
		if form.is_valid():
			print(form)
			return HttpResponseRedirect('')
	else:
		form = Add_Form()
	return render(request, 'add.html', {'form': form})	
	
def register(request):
	form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})

def login(request):
	return render(request, "login.html",{})

def logout(request):
	return render(request, "logout.html",{})