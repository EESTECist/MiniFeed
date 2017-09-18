from django.views import generic
from feed.models import Category, Post


class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['object']
        context['posts'] = category.post_set.all()
        return context
