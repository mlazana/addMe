from django.shortcuts import render

def index(request):
	return render(request, "index.html",{})

def add(request):
	return render(request, "add.html",{})

def contact(request):
	return render(request, "contact.html",{})	