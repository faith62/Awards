from django.shortcuts import get_object_or_404, redirect, render

from awards.forms import AwardsImageForm
from .models import Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
