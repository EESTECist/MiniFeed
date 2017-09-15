from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=200)
    category = models.ForeignKey("Category")
    author = models.ForeignKey(User, blank=False, null=False)

    def __str__(self):
        return "{author}: #{id}".format(author=self.author, id=self.id)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{name}".format(name=self.name)
