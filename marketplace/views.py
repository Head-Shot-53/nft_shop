from django.shortcuts import render
from .models import DigitalArtwork

def artwork_list(request):
    artworks = DigitalArtwork.objects.all()
    return render(request, 'marketplace/artwork_list.html', {'artworks': artworks})