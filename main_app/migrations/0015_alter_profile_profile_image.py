# Generated by Django 5.0.6 on 2024-06-27 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/default_profile_icon.png', null=True, upload_to='profile_images/'),
        ),
    ]
