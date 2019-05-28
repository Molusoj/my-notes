from django.urls import path, include
from . import views

urlpatterns = [

    path('cover', views.cover, name='cover'),
    path('create', views.create, name='create'),
    path('<int:note_id>', views.detail, name='detail')
]
