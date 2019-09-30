from django.conf.urls import url
from basic_app import views

# TEMPLATE urls

urlpatterns=[
	url('register/', views.register, name='register'),
	url('user_login/', views.user_login, name='user_login'),
]