# Generated by Django 4.1.2 on 2023-03-22 14:04

import base.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre2',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=base.models.upload_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Genre3',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=base.models.upload_image_path)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='genre_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre3', to='base.genre'),
        ),
        migrations.AddField(
            model_name='product',
            name='genre_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre2', to='base.genre'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='genre',
        ),
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='base.genre'),
        ),
    ]
