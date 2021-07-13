"""EducoNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as webapp

# region URL apps import
# endregion

urlpatterns = [
    path('', webapp.home, name='home'),
    path('login/', webapp.login_view, name='login'),
    path('logout/', webapp.logout_view, name='logout'),
    path('register/', webapp.register_view, name='register'),
    path('products/', webapp.product, name='products'),
    path('library/', webapp.library, name='library'),
    path('library/book/<int:id>', webapp.book_detail, name='lib-details'),
    path('community/', webapp.community, name='community'),
    path('institutes/', webapp.institute, name='institutes'),
    path('detail/<int:id>', webapp.blog_detail, name='details'),

]
