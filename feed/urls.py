from django.conf.urls import url
from feed.views import IndexView, CategoryDetailView, RegistrationView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^categories/(?P<category_slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category'),
    url(r'^signup/$', RegistrationView.as_view(), name='signup'),
]
