from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
	path('front/',views.store_front,name='store_front'),
	
]