from django.shortcuts import render
from django.http import HttpResponse
from hexlet_django_blog.views import HomePageView
# Create your views here.


# def index(request):
#     return render(request, 'articles/index.html', context={'app_name': 'Article'})


class ArticlePageView(HomePageView):

    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'Article'
        context['tags'] = kwargs.get('tags')
        context['article_id'] = kwargs.get('article_id')
        return context

