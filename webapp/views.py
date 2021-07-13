from django.forms import modelform_factory
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.paginator import Paginator

from .models import Blog, Article, Book, Institute

User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1  # 1 == True
    return render(request, "base/forms.html", {"form": form, 'form_view': "register"})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1  # 1 == True
    return render(request, "base/forms.html", {"form": form, 'form_view': "login"})


def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/login")


@login_required()
def home(request):
    blog_total_count = Blog.objects.count()
    blog_ids = Blog.objects.filter(blog_type__in=['other', 'products'])
    first_blog = blog_ids.first()
    book_count = Blog.objects.count()
    institute_count = Institute.objects.count()
    blog_videos = Blog.objects.filter(video__isnull=False).count()
    article_videos = Article.objects.filter(video__isnull=False).count()
    total_video_count = blog_videos + article_videos

    context = {
        'user': request.user,
        'blog_ids': blog_ids,
        'blog_count': blog_total_count,
        'video_count': total_video_count,
        'first_blog': first_blog,
        'book_count': book_count,
        'institute_count': institute_count,
    }
    return render(request, template_name='base/index.html', context=context)


BlogForm = modelform_factory(Blog, exclude=[])


@login_required()
def blog_detail(request, id):
    article_ids = Article.objects.filter(blog_id=id)
    if article_ids:
        article_ids = sorted(article_ids, key=lambda a: a.pk, reverse=False)
    else:
        article_ids = []
    formBlog = BlogForm()
    blog_id = get_object_or_404(Blog, pk=id)
    # blog_id = Blog.objects.get(pk=id)
    context = {
        'user': request.user,
        'blog_id': blog_id,
        'article_ids': article_ids,
        'formBlog': formBlog,
    }
    return render(request, template_name='details/blogDetails.html', context=context)


@login_required()
def product(request):
    context = {
        'user': request.user,
    }
    return render(request, template_name='product/product.html', context=context)


@login_required()
def library(request):

    if request.is_ajax():
        book = request.POST.get('book')
        qs = Book.objects.filter(name__icontains=book)
        if len(qs) > 0 and len(book) > 0:
            data = []
            for b in qs:
                item = {
                    'pk': b.pk,
                    'name': b.name,
                    'author': b.author,
                }
                data.append(item)
            res = data
        else:
            res = "No se encontraron libros..."
        return JsonResponse({'data': res})

    book_ids = Book.objects.all()
    first_book = Book.objects.first()

    paginator = Paginator(book_ids, 6)  # Show 6 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': request.user,
        'book_list': grouped(page_obj, 3),
        'first_book': first_book,
        'page_obj': page_obj,
    }
    return render(request, template_name='library/library.html', context=context)


@login_required()
def book_detail(request, id):
    book_id = get_object_or_404(Book, pk=id)
    # blog_id = Blog.objects.get(pk=id)

    context = {
        'user': request.user,
        'book_id': book_id,
    }
    return render(request, template_name='details/bookDetails.html', context=context)


@login_required()
def community(request):
    community_ids = Blog.objects.filter(blog_type__exact='community')
    community_total_count = community_ids.count()

    paginator = Paginator(community_ids, 1)  # Show 1 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': request.user,
        'community_count': community_total_count,
        'community_list': grouped(page_obj, 1),
        'page_obj': page_obj,
    }

    return render(request, template_name='community/community.html', context=context)


@login_required()
def institute(request):

    institute_ids = Institute.objects.all()
    first_institute = Institute.objects.first()
    institute_total_count = Institute.objects.count()

    paginator = Paginator(institute_ids, 1)  # Show 1 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': request.user,
        'institute_count': institute_total_count,
        'institute_list': grouped(page_obj, 1),
        'first_institute': first_institute,
        'page_obj': page_obj,
    }

    return render(request, template_name='institute/institute.html', context=context)


def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
