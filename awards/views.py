from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from requests import request

from awards.forms import AwardsImageForm, EditProfileForm, VoteForm
from .models import Image, Profile, Stream
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import resolve, reverse #help identify url name

#api
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    images= Stream.objects.filter(user=user)  #get all stream objects created by user
    # profile = Profile.objects.get(user=user)

    groups_ids= [] #create empty dict

    for image in images:
        groups_ids.append(image.image_id)
    
    image_items = Image.objects.all().order_by('-post_date') #selecting
        
    return render(request,'index.html',{'image_items':image_items,})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = AwardsImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            # image.save()
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

    return render(request,'profile.html',{'images':images_paginator,  'url_name':url_name,'profile':profile,'image_count':image_count,})


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
# @login_required(login_url='/accounts/login/')
# def ProjectDetails(request,image_id):
#     image = get_object_or_404(Image, id=image_id)
#     user=request.user
   

#     return render(request,'project_detail.html',{'image':image, })

@login_required(login_url='/accounts/login')
def ProjectDetails(request,image_id):
   
    image = get_object_or_404(Image, id=image_id)
   
    average_score = round(((image.design + image.usability + image.content)/3),2)

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            image.vote_submissions+=1
            if image.design == 0:
                image.design = int(request.POST['design'])
            else:
                image.design = (image.design + int(request.POST['design']))/2
            if image.usability == 0:
                image.usability = int(request.POST['usability'])
            else:
                image.usability = (image.usability + int(request.POST['usability']))/2
            if image.content == 0:
                image.content = int(request.POST['content'])
            else:
                image.content = (image.content + int(request.POST['usability']))/2

            # image.save()
            return redirect('projectdetails',image_id)
    else:
        form = VoteForm()

    return render(request,'project_detail.html',{'image':image, 'form':form,'average_score':average_score})


#api
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Image.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers =ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)