from django.conf.urls import url
from django.contrib import admin
from feed.views import IndexView, CategoryDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^categories/(?P<category_slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category')
]
