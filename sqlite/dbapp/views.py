from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel
from .forms import MyModelForm  # Import the form class

def create1(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)  # Use form for validation
        if form.is_valid():
            form.save()  # Save the record
            return redirect('readtab')  # Redirect to the read view
    else:
        form = MyModelForm()  # Create an empty form instance
    return render(request, 'create.html', {'form': form})  # Render create template with form

def read(request):
    objects = MyModel.objects.all()  # Get all records
    return render(request, 'read.html', {'objects': objects})  # Render read template with records

def update(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)  # Get the instance to update
    if request.method == 'POST':
        form = MyModelForm(request.POST, instance=instance)  # Use form for validation
        if form.is_valid():
            form.save()  # Save the updated record
            return redirect('readtab')  # Redirect to the read view
    else:
        form = MyModelForm(instance=instance)  # Populate form with existing data
    return render(request, 'update.html', {'form': form, 'instance': instance})  # Render update template

def delete(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)  # Get the instance to delete
    if request.method == 'POST':
        instance.delete()  # Delete the record
        return redirect('readtab')  # Redirect to the read view
    return render(request, 'delete.html', {'instance': instance})  # Render delete confirmation template

def home(request):
    return render(request, 'home.html')