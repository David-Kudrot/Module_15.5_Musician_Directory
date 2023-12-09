# from django.shortcuts import render
# from musician.models import Musician
# from album.models import Album

# def home(request):
#     musicians = Musician.objects.all()  # Fetch all musicians with related albums
#     return render(request, 'home.html', {'musicians': musicians})



from django.shortcuts import render
from musician.models import Musician

def home(request):
    musicians = Musician.objects.prefetch_related('albums')  # Fetch all musicians with related albums
    return render(request, 'home.html', {'musicians': musicians})

