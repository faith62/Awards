from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='indexPage'),
    path('<image_id>',views.ProjectDetails, name='projectdetails'), #name matches the reverse
    path('search/',views.search_image, name='search_results'),
    path('new/image', views.new_image, name='new-image'),
    path('<username>/',views.UserProfile, name='profile'),
    path('profile/edit/', views.EditProfile, name='editprofile'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/project/', views.ProjectList.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 