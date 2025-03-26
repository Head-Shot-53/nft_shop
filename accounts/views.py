from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_artworks')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html')

