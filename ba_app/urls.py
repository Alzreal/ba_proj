from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('RenderAuthor', views.RenderAuthor),
    path('addAuthor', views.addAuthor),
]
