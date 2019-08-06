from django.urls import path, include
from django.conf.urls import url
from . import views
from .models import post
from pprint import pprint

app_name = 'blog'
urlpatterns = [
	path('',views.index, name='indexBlog' ),
    path('<int:post_id>/', views.detail, name='detailBlog'),
]