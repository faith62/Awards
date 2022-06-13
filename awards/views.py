from django.shortcuts import get_object_or_404, redirect, render

from awards.forms import AwardsImageForm, EditProfileForm
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import resolve #help identify url name



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    images = Image.get_all_images().order_by('-post_date')  
    image_items = Image.objects.all().order_by('-post_date') #selecting
    return render(request,'index.html',{'images':images,'image_items':image_items,})

@login_required(login_url='/accounts/login/')
def ProjectDetails(request,image_id):
    image = get_object_or_404(Image, id=image_id)
    user=request.user
   

    return render(request,'project_detail.html',{'image':image, })

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = AwardsImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('indexPage')

    else:
        form = AwardsImageForm()
        
    return render(request, 'new_image.html', {"form": form})

def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name= resolve(request.path).url_name

    if url_name == "profile":
        images = Image.objects.filter(user=user).order_by('-post_date')
    else:
        images = profile.favorites.all()


    #Profile info stats
    image_count = Image.objects.filter(user = user).count()
    

    #Paginator
    paginator = Paginator(images,8)
    page_number = request.GET.get('page')
    images_paginator= paginator.get_page(page_number)

    return render(request,'profile.html',{'images':images_paginator, 'profile':profile, 'url_name':url_name,'image_count':image_count,})


@login_required(login_url='/accounts/login/')
def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.get(user__id=user)
	BASE_WIDTH = 400

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.profile_photo = form.cleaned_data.get('profile_photo')
			profile.first_name = form.cleaned_data.get('first_name')
			profile.last_name = form.cleaned_data.get('last_name')			
			profile.url = form.cleaned_data.get('url')
			profile.bio = form.cleaned_data.get('bio')
			profile.save()
			return redirect('indexPage')
	else:
		form = EditProfileForm()

	
	return render(request, 'edit_profile.html', {'form':form,})

