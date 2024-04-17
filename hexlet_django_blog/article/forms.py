from django import forms
from django.forms import ModelForm
from .models import Article

from hexlet_django_blog.article.models import ArticleComment


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
