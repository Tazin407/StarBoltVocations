from django.db import models
from django.contrib.auth.models import User
# Create your models here.

COMPANY_SIZE=(
    ('1-25 employees','1-25 employees'),
    ('26-50 employees','26-50 employees'),
    ('51-100 employees','51-100 employees'),
    ('100-500 employees','100-500 employees'),
    ('500+ employees','500+ employees'),
)

class Industry(models.Model):
    name= models.CharField(max_length= 40,  unique=True)
    
    def __str__(self) -> str:
        return self.name
    
   
    
class Employer(models.Model):
    user= models.OneToOneField(User,related_name='employer', on_delete=models.CASCADE)
    contact= models.CharField(max_length= 12)
    designation= models.CharField(max_length=20, blank=True)
    industry= models.ForeignKey(Industry, on_delete= models.CASCADE)
    company_name= models.CharField(max_length= 40)
    establish_year= models.IntegerField()
    company_size= models.CharField(max_length= 17, choices= COMPANY_SIZE)
    country= models.CharField(max_length= 40)
    district= models.CharField(max_length= 40)
    address= models.TextField()
    
    def __str__(self) -> str:
        return self.user.first_name