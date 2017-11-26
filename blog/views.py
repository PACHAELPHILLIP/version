from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import *

# Create your views here.
def homeview(request):
    favorite=Article.objects.filter(favorited_by_version=True,published= True)
    article=Article.objects.exclude(favorited_by_version=True,published=True)
    video=Article.objects.filter(video=True,published=True)
    return render (request,'blog/home.html',{"favorite":favorite,"article":article,"video":video})
    

def tagpage(request,tag):
    article = Article.objects.filter(tags__name=tag,published=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(article, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)


    return render (request,'blog/tagpage.html',{'articles':articles,'tag':tag})

def search(request):
    term = request.GET.get("q")
    object_list= Article.objects.filter( Q(title__icontains=term)|Q(body__icontains=term),
        published=True)
    return render(request, 'blog/version_list.html',{"object_list":object_list} )
    

class ArticleListView(ListView):
    queryset = Article.objects.filter(published=True)
    model = Article
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article  


class ArchiveView(ListView):
    model = Article
    paginate_by = 3
    template_name = "article_list.html"


class VersionListView(ListView):
    model = Article
    queryset = Article.objects.filter(category='Version',published=True)
    template_name = "blog/version_list.html"


class TechListView(ListView):
    model = Article
    queryset = Article.objects.filter(category='Tech',published=True)
    template_name = "blog/version_list.html"


class ReviewListView(ListView):
    model = Article
    queryset = Article.objects.filter(category='Review',published=True)
    template_name = "blog/version_list.html"


class MusicListView(ListView):
    model = Article
    queryset = Article.objects.filter(category='Music',published=True)
    template_name = "blog/version_list.html"


class LifestyleListView(ListView):
    model = Article
    queryset = Article.objects.filter(category='Lifestyle',published=True)
    template_name = "blog/version_list.html"


        

