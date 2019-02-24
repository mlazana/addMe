from django.shortcuts import render
from django.http import HttpResponseRedirect
from .addForm import Add_Form
from .models import User, Contact



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
	