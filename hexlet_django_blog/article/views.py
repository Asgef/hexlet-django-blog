from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article
# Create your views here.


# def index(request):
#     return render(request, 'articles/index.html', context={'app_name': 'Article'})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
