# Generated by Django 3.2 on 2021-04-24 03:48

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=webapp.models.Article.video_directory_path, verbose_name='Video del articulo'),
        ),
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=webapp.models.Blog.video_directory_path, verbose_name='Video del blog'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=webapp.models.Article.image_directory_path, verbose_name='Imagen del articulo'),
        ),
    ]
