from django.urls import path
from hexlet_django_blog.article import views
from .views import ArticlePageView


urlpatterns = [
    path('', ArticlePageView.as_view(), name='articles_index'),
]
