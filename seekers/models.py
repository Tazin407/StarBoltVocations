from django.db import models
from django.contrib.auth.models import User
from .constants import EDUCATION, BOARD,GENDER
# Create your models here.



class Seeker(models.Model):
    user= models.OneToOneField(User,related_name='seeker', on_delete= models.CASCADE)
    contact_no= models.CharField(max_length= 12)
    education_level= models.CharField(max_length= 20, choices=EDUCATION)
    board= models.CharField(max_length= 20, choices=BOARD)
    passing_year= models.IntegerField()
    result= models.CharField(max_length= 3)
    group= models.CharField(max_length= 20)
    skillset= models.TextField()
    experience= models.TextField()
    
    
    
class SeekerPersonal(models.Model):
    user= models.OneToOneField(User,related_name='seeker_personal' , on_delete= models.CASCADE)
    country= models.CharField(max_length= 40)
    district= models.CharField(max_length= 40)
    thana= models.CharField(max_length= 40)
    address= models.TextField()
    postal_code= models.IntegerField()
    
    gender= models.CharField(max_length= 20, choices= GENDER)
    date_of_birth= models.DateField()
    
    def __str__(self) -> str:
        return self.user.username
    
