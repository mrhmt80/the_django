from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('about/index.html')
	context = {
		'judul': 'ini halaman about',
		'subjudul' : 'selamat datang :)',
		}
	return HttpResponse(template.render(context, request))
