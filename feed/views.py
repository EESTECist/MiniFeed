from django.views import generic
from feed.models import Category, Post
from feed.forms import PostForm


class IndexView(generic.CreateView):
    form_class = PostForm
    template_name = 'index.html'
    success_url = "."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            post_data = kwargs["data"].copy()
            post_data["author"] = self.request.user.id
            kwargs["data"] = post_data
        return kwargs


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['object']
        context['posts'] = category.post_set.all()
        return context
