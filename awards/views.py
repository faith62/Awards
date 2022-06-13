from django.shortcuts import get_object_or_404, render
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

