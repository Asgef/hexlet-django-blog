from django.urls import path
from hexlet_django_blog.article import views
from .views import ArticlePageView


urlpatterns = [
    path('<str:tags>/<int:article_id>/', ArticlePageView.as_view(), name='article'),
]
