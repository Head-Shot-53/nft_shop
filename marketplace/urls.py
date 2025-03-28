from django.urls import path
from . import views

urlpatterns = [
    path('artworks_list/',views.artwork_list, name='artwork_list'),
    path('my-artworks/', views.my_artworks, name='my_artworks'),
    path('', views.home, name='home'),
    path('create-artwork/', views.create_artwork, name='create_artwork'),
    path('artwork/<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
    path('artwork/<int:artwork_id>/delete/', views.delete_artwork, name='delete_artwork'),
    path('artwork/<int:artwork_id>/edit/', views.edit_artwork, name='edit_artwork'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.artworks_by_category, name='artworks_by_category'),

]