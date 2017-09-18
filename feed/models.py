from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Post(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=200)
    category = models.ForeignKey("Category")
    author = models.ForeignKey(User, blank=False, null=False)

    def __str__(self):
        return "{author}: #{id}".format(author=self.author, id=self.id)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{name}".format(name=self.name)


@receiver(pre_save, sender=Category)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        if hasattr(sender, "name"):
            instance.slug = slugify(instance.name)
        else:
            raise AttributeError("Name field is required for slug.")
    return instance
