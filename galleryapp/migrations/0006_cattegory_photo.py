# Generated by Django 5.1 on 2024-09-03 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0005_gallery_delete_animals_delete_background_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cattegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='photo_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleryapp.cattegory')),
            ],
        ),
    ]
