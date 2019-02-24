from django.shortcuts import render
from django.http import HttpResponse
from .addForm import Add_Form



def index(request):
	return render(request, "index.html",{})

def contact(request):
	return render(request, "contact.html",{})

def add(request):        
	form = Add_Form()
	return render(request, 'add.html', {"form": form})	
	