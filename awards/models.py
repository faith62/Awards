from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.urls import reverse

def user_directory_path(instance, filename):
    #this file will be uploaded to MEDIA_ROOT/user(id/filename)
    return 'user_{0}/{1}'.format(instance.user.id,filename)

# Create your models here.
class Image(models.Model):    
    image_name =models.CharField(max_length=50)
    image_description =models.CharField(max_length=500)
    pic=models.ImageField(upload_to=user_directory_path,blank=True,null = True)
    # post = HTMLField(blank=True,null = True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null = True,)
    post_date = models.DateTimeField(auto_now_add=True,blank=True,null = True,)
    likes = models.IntegerField(blank=True,null = True,)
    url=models.CharField(max_length=80,blank=True,null = True,)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('imagedetails',args=[str(self.id)])#clickto image get to imagedetails url
    @classmethod
    def update_image(cls, id ,image_name, image_description ,url,pic,user,):
        update = cls.objects.filter(id = id).update(image_name=image_name, image_description=image_description, pic=pic, user=user)
 
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_by_image_category(cls,image_category):
        images = cls.objects.filter(image_category__name__icontains=image_category)
        return images

    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null = True,)
    first_name = models.CharField(max_length=50,blank=True,null = True,)
    last_name = models.CharField(max_length=50,blank=True,null = True,)
    bio=models.CharField(max_length=500)
    profile_photo=models.ImageField(upload_to='profile/',blank=True,null = True,)
    url=models.CharField(max_length=50,blank=True,null = True,)
    created =models.DateField(auto_now_add=True,blank=True,null = True,)

    def __str__(self):
        return self.first_name

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # def save_user_profile(sender,instance, **kwargs):
    #     instance.profile.save()

    # def save_profile(self):
    #     self.save()

    # def delete_profile(self):
    #     self.delete()
    # post_save.connect(create_user_profile, sender=User)
    # post_save.connect(save_user_profile, sender=User)

 