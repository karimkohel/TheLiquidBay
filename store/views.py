from django.shortcuts import render
from .models import Liquid

# Create your views here.

def store_front(request):
	context = {
	'title':'Store',
	'store': True,
	'liquids': Liquid.objects.all()
	}
	return render(request,'store/front.html',context)