from django.db import models
from django.contrib.auth.models import User

class DigitalArtwork(models.Model):
    ART_TYPE_CHOICES = [
        ('image', 'Картинка'),
        ('animation', 'Анімація'),
        ('music', 'Музика'),
        ('model3d', '3D модель'),
        ('other', 'Інше')
    ]

    # STATUS_CHOICES = [
    #     ('available', 'Доступно'),
    #     ('sold', 'Продано'),
    #     ('hiden', 'Приховано'),
    # ]

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    art_type = models.CharField(max_length=20, choices=ART_TYPE_CHOICES)
    file = models.FileField(upload_to='artworks/')
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title