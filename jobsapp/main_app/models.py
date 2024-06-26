from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    header = models.CharField(max_length=30)
    subheader = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    about = models.TextField(max_length=250)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # Add this line


    def __str__(self):
        return self.header


class EduHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name_school = models.CharField(max_length=30)
    name_major = models.CharField(max_length=30)
    date_start = models.DateField('Start Date')
    date_end = models.DateField('End Date', null=True, blank=True)

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
    name = models.CharField(max_length=30)
    about = models.TextField(max_length=250)
    location = models.CharField(max_length=60)
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

    def __str__(self):
        return f"{self.name}"



class JobHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    date_start = models.DateField('Start Date')
    date_end = models.DateField('End Date', null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    def end_date_display(self):
        return self.date_end if self.date_end else "Present"






