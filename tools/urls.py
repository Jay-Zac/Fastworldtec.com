from django.urls import path
from . import views

app_name = 'tools'
urlpatterns = [
    path('', views.tools_view, name='items4'),
]
