from django.views import generic
from feed.models import Category, Post
from feed.forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


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


class RegistrationView(generic.FormView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, new_user)
        return super().form_valid(form)
