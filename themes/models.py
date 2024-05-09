from django.db import models
from django.contrib.auth.models import User
from core.models import Category


class Item(models.Model):
    objects = None
    category = models.ForeignKey(Category, related_name='items2', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    affiliate_link = models.CharField(max_length=2083, blank=False, null=False)
    image = models.ImageField(upload_to='themes_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items2', on_delete=models.CASCADE)
    created_at = models. DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
