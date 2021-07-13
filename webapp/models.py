from datetime import datetime

from django.conf import settings
from django.db import models

STATUS = [('draft', 'Nuevo'), ('available', 'Disponible'), ('cancel', 'Deshabilitado')]
BLOG_TYPE = [('other', 'Variado'), ('products', 'Oferta educativa'), ('library', 'Biblioteca'), ('institute', 'Institución'), ('community', 'Comunidad')]
# Create your models here.


class Blog(models.Model):

    def image_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/images/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    def video_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/videos/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(max_length=5000, verbose_name="Description")
    image = models.ImageField(upload_to=image_directory_path, verbose_name="Imagen del blog", null=True, blank=True)
    video = models.FileField(upload_to=video_directory_path, verbose_name="Video del blog", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    write_date = models.DateTimeField(auto_now=True, verbose_name="Ultima Modificacion")
    status = models.CharField(max_length=20, choices=STATUS, default='draft', verbose_name="Estado")
    blog_type = models.CharField(max_length=20, choices=BLOG_TYPE, null=True, default='other', verbose_name="Tipo")

    def __str__(self):
        return self.name


class Article(models.Model):

    def image_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/images/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    def video_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/videos/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name="Titulo")
    text_content = models.TextField(max_length=20000, verbose_name="Contenido")
    image = models.ImageField(upload_to=image_directory_path, verbose_name="Imagen del articulo", null=True, blank=True)
    video = models.FileField(upload_to=video_directory_path, verbose_name="Video del articulo", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    write_date = models.DateTimeField(auto_now=True, verbose_name="Ultima Modificacion")
    status = models.CharField(max_length=10, choices=STATUS, default='draft', verbose_name="Estado")
    blog_id = models.ForeignKey(Blog, verbose_name="Blog", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.blog_id.name + ' - ' + self.name


class Book(models.Model):

    def image_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/images/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    def file_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/books/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, verbose_name="Titulo")
    author = models.CharField(max_length=200, verbose_name="Autor")
    image = models.ImageField(upload_to=image_directory_path, verbose_name="Imagen", null=True, blank=True)
    file = models.FileField(upload_to=file_directory_path, verbose_name="Archivo", null=True, blank=True)

    def __str__(self):
        return self.name


class Institute(models.Model):

    def image_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/images/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    def video_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/videos/user_{1}/{2}'.format(settings.MEDIA_ROOT, instance.user.id, filename)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(max_length=20000, verbose_name="Sobre")
    image = models.ImageField(upload_to=image_directory_path, verbose_name="Logo", null=True, blank=True)
    # video = models.FileField(upload_to=video_directory_path, verbose_name="Video de presentación", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    write_date = models.DateTimeField(auto_now=True, verbose_name="Ultima Modificacion")

    def __str__(self):
        return self.name


