from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserPostForm
from .models import UserPost
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
	template = loader.get_template('user_post/index.html')
	context = {
		'judul': 'halaman user',
	}
	return HttpResponse(template.render({},request))

# def create(request):
# 	template = loader.get_template('user_post/create.html')
# 	context = {
#         'judul': 'halaman user',
#     }
# 	return HttpResponse(template.render({},request))

# def create(request):
# 	if request.method == 'POST':
# 		form = UserPostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			# handle_uploaded_file(request.FILES['file'])
# 			print("Hello World")
# 			form.save()
# 			return HttpResponseRedirect('image upload success')
# 	else:
# 		form = UserPostForm()
# 	return render(request, 'user_post/create.html', {'form': form})

# def create(request):
# 		if request.method == 'POST':
# 			if request.POST.get('nama') and request.POST.get('picture'):
# 				print(request.POST.get('nama'))
# 				post=UserPost()
# 				post.nama= request.POST.get('nama')
# 				post.picture= request.POST.get('picture')
# 				post.save()
				
# 				# return render(request, 'user_post/create.html')  
# 				return HttpResponse('image upload success')
# 		else:
# 			return render(request,'user_post/create.html')

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