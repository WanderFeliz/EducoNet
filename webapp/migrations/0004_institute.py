# Generated by Django 3.2 on 2021-06-25 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(max_length=20000, verbose_name='Sobre')),
                ('image', models.ImageField(blank=True, null=True, upload_to=webapp.models.Institute.image_directory_path, verbose_name='Logo')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('write_date', models.DateTimeField(auto_now=True, verbose_name='Ultima Modificacion')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
