from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    full_name = models.CharField(max_length=30)
    headline = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    about = models.TextField(max_length=1000)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default_profile_icon.png', null=True, blank=True)

    def __str__(self):
        return self.full_name


class EduHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name_school = models.CharField(max_length=30)
    name_major = models.CharField(max_length=30)
    date_start = models.DateField('Start Date')
    date_end = models.DateField('End Date', null=True, blank=True)
    school_image = models.ImageField(upload_to='school_images/', default='school_images/default_school_icon.png', null=True, blank=True)

    def __str__(self):
        return f"{self.name_school} at {self.name_major}"

    def end_date_display(self):
        return self.date_end if self.date_end else "Present"


INDUSTRIES = (
    ('Finance', 'Finance'),
    ('Software', 'Software'),
    ('Healthcare', 'Healthcare'),
)

EMPLOYEE_COUNT = (
    ('0 - 10', '0 - 10'),
    ('10 - 50', '10 - 50'),
    ('50 - 250', '50 - 250'),
    ('250 - 1000', '250 - 1000'),
    ('1000+', '1000+'),
)


class Company(models.Model):
    page_owners = models.ManyToManyField(User, related_name='companies')
    name = models.CharField(max_length=30)
    about = models.TextField(max_length=1000)
    location = models.CharField(max_length=60)
    company_image = models.ImageField(upload_to='company_images/', default='company_images/default_company_icon.png', null=True, blank=True)
    employee_count = models.CharField(
        max_length=20,
        choices=EMPLOYEE_COUNT,
        default=EMPLOYEE_COUNT[0][0]
    )
    industry = models.CharField(
        max_length=20,
        choices=INDUSTRIES,
        default=INDUSTRIES[0][0]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.name}"



class JobHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    date_start = models.DateField('Start Date')
    date_end = models.DateField('End Date', null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    def end_date_display(self):
        return self.date_end if self.date_end else "Present"

    def get_company_image_url(self):
        return self.company.company_image.url if self.company.company_image else None






