from django.shortcuts import render, redirect, get_object_or_404
from .models import DigitalArtwork, Category
from .forms import ArtWorksStatusForms, ArtWorkCreateForm
from django.contrib.auth.decorators import login_required
from .commands import PublishArtWorkCommand, MarkAsSoldCommand, SetDraftCommand

def home(request):
    return render(request, 'marketplace/home.html')

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


@login_required
def create_artwork(request):
    if request.method == 'POST':
        form = ArtWorkCreateForm(request.POST,request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.author = request.user
            artwork.save()
            return redirect('my_artworks')
    else:
        form = ArtWorkCreateForm()

    return render(request, 'marketplace/create_artwork.html', {'form':form})

def artwork_detail(request, artwork_id):
    artwork = get_object_or_404(DigitalArtwork, id=artwork_id)
    return render(request, 'marketplace/artwork_detail.html', {'artwork': artwork})

@login_required
def delete_artwork(request, artwork_id):
    artwork = get_object_or_404(DigitalArtwork, id=artwork_id, author=request.user)
    if request.method == 'POST':
        artwork.delete()
        return redirect('my_artworks')
    return redirect('artwork_detail',artwork_id=artwork_id)

@login_required
def edit_artwork(request, artwork_id):
    artwork = get_object_or_404(DigitalArtwork, id=artwork_id, author=request.user)

    if request.method == 'POST':
        form = ArtWorkCreateForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_detail', artwork_id=artwork.id)
    else:
        form = ArtWorkCreateForm(instance=artwork) 

    return render(request, 'marketplace/edit_artwork.html', {'form': form, 'artwork': artwork})

def category_list(request):
    parent_categories = Category.objects.filter(parent__isnull=True).prefetch_related('children')
    return render(request, 'marketplace/category_list.html', {'categories': parent_categories})

def artworks_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    artworks = DigitalArtwork.objects.filter(category=category)

    return render(request, 'marketplace/artworks_by_category.html', {
        'category': category,
        'artworks': artworks
    })


@login_required
def change_artwork_status(request):
    if request.method == 'POST':
        artwork_id = request.POST.get('artwork_id')
        new_status = request.POST.get('status')
        
        artwork = get_object_or_404(DigitalArtwork, id=artwork_id, author = request.user)

        command_map = {
            'draft':SetDraftCommand,
            'published':PublishArtWorkCommand,
            'sold':MarkAsSoldCommand,
        }

        command_class = command_map.get(new_status)

        if command_class:
            command = command_class(artwork)
            command.execute()


        return redirect('my_artworks')
    
