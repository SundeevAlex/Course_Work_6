from django.views.generic import ListView
from blog.models import BlogArticle


class BlogArticleListView(ListView):
    """
    Контроллер для просмотра списка статей блога
    """
    model = BlogArticle
