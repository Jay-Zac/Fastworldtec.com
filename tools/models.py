from django.db import models
from django.contrib.auth.models import User
from core.models import Category


class Item(models.Model):
    objects = None
    category = models.ForeignKey(Category, related_name='items4', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='items4', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    introduction = models.TextField(blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    affiliate_link = models.CharField(max_length=2083, blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='tools_images', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
