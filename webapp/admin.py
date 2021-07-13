from django.contrib import admin
from . models import Article, Blog, Book, Institute

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        return form


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(ArticleAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        return form


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(BookAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        return form


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(InstituteAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        return form