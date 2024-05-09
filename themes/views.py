from django.db.models import Q
from django.shortcuts import render
from .models import Item
from core.models import Category


def themes_view(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'themes.html', {'items': items,
                                           'query': query,
                                           'categories': categories,
                                           'category_id': int(category_id)
                                           })
