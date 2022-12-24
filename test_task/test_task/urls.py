from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('menu.urls', namespace='menu')),
    path('admin/', admin.site.urls),
]
