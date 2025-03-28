from django import forms
from .models import DigitalArtwork

class ArtWorksStatusForms(forms.ModelForm):
    class Meta:
        model = DigitalArtwork
        fields = ['status']

class ArtWorkCreateForm(forms.ModelForm):
    class Meta:
        model = DigitalArtwork
        fields = ['title', 'description', 'price', 'art_type', 'file', 'status', 'category']