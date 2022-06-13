from django.contrib import admin
from .models import Image,Profile

class ImageAdmin(admin.ModelAdmin):    
   
    list_display = ('image_name', 'pic')

# Register your models here.
admin.site.register(Image, ImageAdmin)
admin.site.register(Profile)


admin.site.site_header='Project-awards admin'
admin.site.site_title='PA'
admin.site.index_title='Welcome to Projects-Awards admin'