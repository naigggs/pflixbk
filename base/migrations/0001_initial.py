# Generated by Django 4.1.2 on 2023-02-01 17:37

import base.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=base.models.upload_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=base.models.upload_image_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=base.models.upload_video_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.director')),
                ('genre', models.ManyToManyField(blank=True, to='base.genre')),
            ],
        ),
    ]
