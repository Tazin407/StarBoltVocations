from django.db import models
from employers.models import Employer
from .import constants
from seekers.models import Seeker

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length= 40, unique=True)
    
    def __str__(self) -> str:
        return self.name

class Job(models.Model):
    title= models.CharField(max_length= 40)
    category= models.ForeignKey(Category, on_delete= models.CASCADE, unique=False)
    description = models.TextField()
    requirements= models.TextField()
    responsibility= models.TextField()
    location= models.CharField(max_length= 40)
    status= models.CharField(choices= constants.STATUS, max_length= 40)
    typeo= models.CharField(choices= constants.TYPE, max_length= 40, null= True)
    date= models.DateField(auto_now_add= True)
    deadline= models.DateField(null= True)
    employer= models.ForeignKey(Employer, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
class ApplyJob(models.Model):
    candidate= models.ForeignKey(Seeker, on_delete= models.CASCADE)
    job= models.ForeignKey(Job, on_delete= models.CASCADE)
    experience= models.CharField(max_length= 100)
    cv= models.FileField(upload_to='static/uploaded_cv/')
    
    def __str__(self) -> str:
        return self.candidate.user.username