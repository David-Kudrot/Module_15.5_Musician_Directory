from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import Musician

# Create your views here.

def musician_views(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('musician')
    else:
        musician_form = MusicianForm()
    return render(request, 'musician.html', {'form': musician_form})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    return render(request, 'musician.html', {'form': musician_form})
 