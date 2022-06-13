from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='indexPage'),
    path('<image_id>',views.ProjectDetails, name='projectdetails'), #name matches the reverse

]