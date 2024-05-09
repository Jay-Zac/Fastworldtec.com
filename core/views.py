from django.shortcuts import render
from .models import Category, Review
from .models import Item


def core_view(request):
    items = Item.objects.filter(is_sold=False)[:5]
    reviews = Review.objects.all()

    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
        'reviews': reviews,
    })


def about_view(request):
    return render(request, 'about.html')
