from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:tweet_id>/edit/', views.edit, name='edit'),
    path('<int:tweet_id>/delete/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
]