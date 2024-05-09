from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('software/', include('software.urls')),
    path('themes/', include('themes.urls')),
    path('courses/', include('courses.urls')),
    path('tools/', include('tools.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]
