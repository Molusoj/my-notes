from django.urls import path, include
from . import views

urlpatterns = [

    path('cover', views.cover, name='cover'),
    path('create', views.create, name='create')
]
