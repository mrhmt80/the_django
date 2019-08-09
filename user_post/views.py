from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserPostForm
from .models import UserPost
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
	user_post_list = UserPost.objects.order_by('-id')[:5]
	template = loader.get_template('user_post/index.html')
	context = {
		'user_post_list': user_post_list,
	}
	return HttpResponse(template.render(context, request))

def create(request):
	if request.method == 'POST':
		form = UserPostForm(request.POST, request.FILES)
		if form.is_valid():
			obj = UserPost()
			obj.nama = form.cleaned_data['nama']
			obj.picture = form.cleaned_data['picture']
			obj.save()
			return HttpResponseRedirect('/user_post/create',{'form':form})

	else:
		form = UserPostForm()
	return render(request, 'user_post/create.html', {'form': form})

def edit(request, user_post_id):
	# user_post_list = UserPost.objects.get(id=user_post_id)
	# template = loader.get_template('user_post/edit.html')
	# context = {
	# 	'user_post_list': user_post_list,
	# }
	if request.method == 'POST':
		form = UserPostForm(request.POST, request.FILES)
		if form.is_valid():
			obj = UserPost.objects.get(id=user_post_id)
			obj.nama = form.cleaned_data['nama']
			obj.picture = form.cleaned_data['picture']
			obj.save()
			return HttpResponseRedirect('/user_post/',{'form':form})

	else:
		form = UserPostForm()
	return render(request, 'user_post/edit.html', {'form': form})