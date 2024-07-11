from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogArticleListView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogArticleListView.as_view(), name='list'),
]
