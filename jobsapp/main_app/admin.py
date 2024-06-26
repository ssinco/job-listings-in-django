from django.contrib import admin

from .models import Profile, JobHistory, EduHistory, Company

# Register your models here.

admin.site.register(Profile)
admin.site.register(JobHistory)
admin.site.register(EduHistory)
admin.site.register(Company)


