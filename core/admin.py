from django.contrib import admin
from .models import Category, Review, Item

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Item)

admin.site.site_title = 'fastworldtec'
admin.site.site_header = 'fastworldtec Admin'
admin.site.index_title = 'Admin'
