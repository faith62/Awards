from django import forms
from .models import  Image, Profile

class AwardsImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date']
        widgets = {
            'image_name':forms.TextInput(),
            'image_caption':forms.TextInput(),
           
        }

class EditProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)
    first_name = forms.CharField(widget=forms.TextInput(), max_length=50,required=False)
    last_name =forms.CharField(widget=forms.TextInput(), max_length=50,required=False)
    url =forms.URLField(widget=forms.TextInput(), max_length=60,required=False)
    bio=forms.CharField(widget=forms.TextInput(), max_length=260,required=False)

    class Meta:
        model = Profile
        fields = ('profile_photo','first_name','last_name','url', 'bio' )

class VoteForm(forms.ModelForm):
     class Meta:
        model = Image
        fields = ('design','usability','content')