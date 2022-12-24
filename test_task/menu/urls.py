from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:menu_slug>/', views.menu, name='menu'),
    path('<slug:menu_slug>/<slug:fl_slug>/', views.first, name='fl'),
    path(
        '<slug:menu_slug>/<slug:fl_slug>/<slug:sl_slug>/',
        views.second, name='sl'
    ),
    path(
        '<slug:menu_slug>/<slug:fl_slug>/<slug:sl_slug>/<slug:tl_slug>/',
        views.third, name='tl'
    ),
]