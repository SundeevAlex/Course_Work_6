from django.views.generic import ListView, DetailView
from blog.models import BlogArticle


class BlogArticleListView(ListView):
    """
    Контроллер для просмотра списка статей блога
    """
    model = BlogArticle


class BlogArticleDetailView(DetailView):
    """
    Контроллер для просмотра статьи блога
    """
    model = BlogArticle

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
