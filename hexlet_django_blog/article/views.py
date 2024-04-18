from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import CommentArticleForm, ArticleCommentForm, ArticleForm

from hexlet_django_blog.article.models import Article
from django.contrib import messages
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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ваша статья добавлена")
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ваша статья обновлена")
            return redirect('articles')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.object.get(id=article_id)
        if article:
            article.delete()
            messages.add_message(request, messages.SUCCESS, f"Статья: {article.name} удалена")
        return redirect('article')
