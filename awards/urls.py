from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='indexPage'),
    path('<image_id>',views.ProjectDetails, name='projectdetails'), #name matches the reverse
    path('new/image', views.new_image, name='new-image'),
     path('<username>/',views.UserProfile, name='profile'),
    path('profile/edit/', views.EditProfile, name='editprofile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 