from django.urls import path
from .views import index, ArticleDetail	
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.ArticleDetail, name='article'),
    path('search/', views.search_news, name='search_news'),
    path('about/', views.about, name='about'),
]