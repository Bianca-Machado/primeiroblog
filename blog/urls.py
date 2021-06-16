from django.urls import path
from . import views

name_app = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
]