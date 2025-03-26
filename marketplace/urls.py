from django.urls import path
from . import views

urlpatterns = [
    path('artworks_list/',views.artwork_list, name='artwork_list'),
    path('my-artworks/', views.my_artworks, name='my_artworks'),
    path('', views.home, name='home')
]