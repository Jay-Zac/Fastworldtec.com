from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    objects = None
    category = models.ForeignKey(Category, related_name='items1', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    affiliate_link = models.CharField(max_length=2083, blank=False, null=False)
    image = models.ImageField(upload_to='core_software_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items1', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Review(models.Model):
    objects = None
    image = models.ImageField(upload_to='review_images', blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    affiliate_link = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
