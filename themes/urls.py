from django.urls import path
from . import views

app_name = 'themes'
urlpatterns = [
    path('', views.themes_view, name='items2'),
]
