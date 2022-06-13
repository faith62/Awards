from rest_framework import serializers
from .models import Profile,Image

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_photo', 'all_images')
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_name', 'image_description', 'user', 'url')
