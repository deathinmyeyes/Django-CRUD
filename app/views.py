from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
# Create your views here.

def list(request):
    cars = Car.objects.all()
    return render(request, 'main.html', {'cars': cars})


def create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = CarForm()
    return render(request, 'create.html', {'form': form})

def update(request, id):
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = CarForm(instance=car)
    return render(request, 'create.html', {'form': form})

def delete(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('list')