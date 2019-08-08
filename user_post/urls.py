from django.urls import path, include
from django.conf.urls import url
from . import views
# from .models import post
from pprint import pprint

app_name = 'user_post'
urlpatterns = [
	path('',views.index, name='indexUser' ),
	path('create/',views.create, name='createUser' ),
	# path('insert/',views.insert),
	# path('edit/<int:id>', views.edit),
	# path('update/<int:id>', views.update),  
	# path('delete/<int:id>', views.delete),  
]