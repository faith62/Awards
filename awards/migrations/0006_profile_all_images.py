# Generated by Django 4.0.5 on 2022-06-13 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_remove_image_likes_image_content_image_design_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='all_images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.image'),
        ),
    ]