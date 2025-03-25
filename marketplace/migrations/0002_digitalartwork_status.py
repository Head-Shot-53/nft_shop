# Generated by Django 5.1.7 on 2025-03-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalartwork',
            name='status',
            field=models.CharField(choices=[('available', 'Доступно'), ('sold', 'Продано'), ('hiden', 'Приховано')], default='available', max_length=20),
        ),
    ]
