from typing import Any
from django import forms 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .import models
from .models import COMPANY_SIZE

class EmployerRegistration(UserCreationForm):
    
    industry = forms.ModelChoiceField(queryset=models.Industry.objects.all())
    contact= forms.IntegerField()
    company_name= forms.CharField()
    establish_year= forms.IntegerField()
    company_size= forms.ChoiceField(choices= COMPANY_SIZE)
    country= forms.CharField()
    district= forms.CharField()
    address= forms.CharField()
    class Meta:
        model= models.User
        fields = ['username','first_name', 'last_name', 'email', 'contact', 'company_name', 'industry', 'establish_year', 'company_size', 'address', 'district', 'country']
      

    def save(self, commit=True):
        our_user= super().save(commit=False) 
        if commit==True:
            our_user.save()
            contact= self.cleaned_data.get('contact')
            company_name= self.cleaned_data.get('company_name')
            address= self.cleaned_data.get('address')
            industry= self.cleaned_data.get('industry')
            establish_year= self.cleaned_data.get('establish_year')
            company_size= self.cleaned_data.get('company_size')
            district= self.cleaned_data.get('district')
            country= self.cleaned_data.get('country')
            
            forms.Employer.objects.create(
                user= our_user,
                contact= contact,
                company_name= company_name,
                address=address,
                industry= industry,
                establish_year= establish_year,
                company_size= company_size,
                district= district,
                country= country,
            )
        return our_user
        
        
class EmployerUpdateForm(UserChangeForm):
    contact= forms.CharField()
    designation= forms.CharField()
    industry= forms.ModelChoiceField(queryset=models.Industry.objects.all())
    company_name= forms.CharField()
    establish_year= forms.IntegerField()
    company_size= forms.ChoiceField( choices= COMPANY_SIZE)
    country= forms.CharField()
    district= forms.CharField()
    address= forms.CharField()
    
    class Meta:
        model= models.User
        fields = ['username','first_name', 'last_name', 'email', 'contact','designation','industry', 'company_name', 'establish_year', 'company_size', 'country', 'district', 'address',]
        exclude=['password']
        
        def __init__(self, *args: Any, **kwargs) :
            self.fields['password'].disabled = True 
            super().__init__(*args, **kwargs)
     
    def save(self, commit=True):
        our_user= super().save(commit=False)
        if commit:
            our_user.save()
            
            our_user_account, created= models.Employer.objects.get_or_create(user= our_user)
            our_user_account.contact= self.cleaned_data.get('contact')
            our_user_account.designation= self.cleaned_data.get('designation')
            our_user_account.industry= self.cleaned_data.get('industry')
            our_user_account.company_name= self.cleaned_data.get('company_name')
            our_user_account.establish_year= self.cleaned_data.get('establish_year')
            our_user_account.company_size= self.cleaned_data.get('company_size')
            our_user_account.country= self.cleaned_data.get('country')
            our_user_account.district= self.cleaned_data.get('district')
            our_user_account.address= self.cleaned_data.get('address')
            
            our_user_account.save()
            
        return our_user
            
        
        