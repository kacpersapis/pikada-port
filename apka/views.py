from django.shortcuts import render, get_object_or_404, redirect
from .models import Trip, Task
from .forms import TripForm, TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def caly_grafik(request):
    wszystkie = Trip.objects.all()
    return render(request, 'grafik.html', {'grafik': wszystkie})

@login_required
def nowa_wycieczka(request):
    form = TripForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    return render(request, 'wycieczka_form.html', {'form': form, 'nowy': True})

@login_required
def edytuj_wycieczke(request, id):
    wycieczka = get_object_or_404(Trip, pk=id)
    form = TripForm(request.POST or None, request.FILES or None, instance=wycieczka)

    if form.is_valid():
        form.save()
        return redirect(caly_grafik)
    return render(request, 'wycieczka_form.html', {'form': form, 'nowy': False})

@login_required
def usun_wycieczke(request, id):
    wycieczka = get_object_or_404(Trip, pk=id)

    if request.method == "POST":
        wycieczka.delete()
        return redirect(caly_grafik)

    return render(request, 'potwierdz.html', {'wycieczka': wycieczka})

def lista(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(lista)

    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form =TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(lista)

    context = {'form': form}

    return render(request, 'update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect(lista)

    context = {'item': item}
    return render(request, 'delete.html', context)