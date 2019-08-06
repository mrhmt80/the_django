from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import post
from django.urls import reverse

# Create your views here.
def index(request):
	latest_post_list = post.objects.order_by('-id')[:5]
	template = loader.get_template('blog/index.html')
	context = {
		'latest_post_list': latest_post_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, post_id):
	    post_detail = get_object_or_404(post, pk=post_id)
	    return render(request, 'blog/detail.html', {'post': post_detail})