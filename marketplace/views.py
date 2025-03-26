from django.shortcuts import render, redirect
from .models import DigitalArtwork
from .forms import ArtWorksStatusForms
from django.contrib.auth.decorators import login_required

def artwork_list(request):
    artworks = DigitalArtwork.objects.filter(status = 'available')
    return render(request, 'marketplace/artwork_list.html', {'artworks': artworks})

@login_required
def my_artworks(request):
    artworks = DigitalArtwork.objects.filter(author = request.user)

    if request.method == 'POST':
        artwork_id = request.POST.get('artwork_id')
        artwork = DigitalArtwork.objects.get(id=artwork_id, author=request.user)
        form = ArtWorksStatusForms(request.POST, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('my_artworks')
    else:
        form = ArtWorksStatusForms()

    return render(request, 'marketplace/my_artworks.html', {
        'artworks':artworks,
        'form':form
    })


def home(request):
    return render(request, 'marketplace/home.html')