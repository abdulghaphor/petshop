from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {
		'pets': Pet.objects.filter(available=True)
	}
	return render(request,'index.html',context)


def pet_add(request):
	if request.method == 'POST':
		form = PetForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	context = {
		'form' : PetForm()
	}
	return render(request,'pet_add.html',context)

def pet_delete(request,pet_id):
	Pet.objects.get(id=pet_id).delete()
	return redirect('index')
		

def pet_details(request,pet_id):
	context = {
		'pet' : Pet.objects.get(id=pet_id)
	}
	return render(request,'pet_details.html',context)

def pet_update(request,pet_id):
	form = PetForm(instance=Pet.objects.get(id=pet_id))
	if request.method == 'POST':
		form = PetForm(request.POST,request.FILES,instance=Pet.objects.get(id=pet_id))
		if form.is_valid():
			pet = form.save(commit=False)
			pet.available = True
			pet.save()
			return redirect('pet-details',pet_id)
	context = {
		'pet' : Pet.objects.get(id=pet_id),
		'form' : form
	}
	return render(request,'pet_update.html',context)