from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CommentArticleForm, ArticleCommentForm

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


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])

        return render( ... )


class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        return render(request, 'comment.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            comment = Comment(
                name=form.cleaned_data['content'],
            )
            comment.save()


class ArticleCommentFormView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content = check_for_spam(form.data['content'])
            form.save()
