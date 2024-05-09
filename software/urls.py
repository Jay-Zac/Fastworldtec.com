from django.urls import path
from . import views

app_name = 'software'
urlpatterns = [
    path('', views.software_view, name='items'),
]
