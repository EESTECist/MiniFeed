from django.conf.urls import url
from django.contrib import admin
from feed import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
