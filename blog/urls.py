from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogArticleListView
from django.views.decorators.cache import cache_page

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(BlogArticleListView.as_view()), name='list'),
]
