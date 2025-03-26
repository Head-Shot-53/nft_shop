from django import forms
from .models import DigitalArtwork

class ArtWorksStatusForms(forms.ModelForm):
    class Meta:
        model = DigitalArtwork
        fields = ['status']
        