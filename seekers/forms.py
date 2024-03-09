from typing import Any
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .import models
from .import constants

class SeekerRegistration(UserCreationForm):
    contact_no = forms.CharField()
    education_level= forms.ChoiceField( choices=constants.EDUCATION)
    board= forms.ChoiceField( choices=constants.BOARD)
    passing_year= forms.IntegerField()
    result = forms.CharField()
    group= forms.CharField()
    skillset= forms.CharField()
    experience= forms.CharField()
    
    
    country= forms.CharField()
    district= forms.CharField()
    thana= forms.CharField()
    address= forms.CharField()
    postal_code= forms.CharField()
    gender= forms.ChoiceField( choices= constants.GENDER)
    date_of_birth= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model= models.User
        fields = ['username','first_name', 'last_name', 'email', 'contact_no','gender','date_of_birth', 'education_level', 'board', 'passing_year', 'result', 'group', 'skillset', 'experience', 'district', 'thana', 'country','postal_code','address']
      
    def save(self, commit=True):
        our_user= super().save(commit=False)
        if commit==True:
            our_user.save()
            user= self.cleaned_data.get('user')
            contact_no=self.cleaned_data.get('contact_no') 
            education_level=self.cleaned_data.get('education_level') 
            board=self.cleaned_data.get('board')
            passing_year=self.cleaned_data.get('passing_year') 
            result=self.cleaned_data.get('result') 
            group=self.cleaned_data.get('group')
            skillset=self.cleaned_data.get('skillset') 
            experience=self.cleaned_data.get('experience') 
            
            models.Seeker.objects.create(
                user  = our_user,
                contact_no = contact_no,
                education_level = education_level,
                board = board,
                passing_year = passing_year,
                result = result,
                group = group,
                skillset = skillset,
                experience = experience,
            )
            
            country= self.cleaned_data.get('country')
            district= self.cleaned_data.get('district')
            thana= self.cleaned_data.get('thana')
            address= self.cleaned_data.get('address')
            postal_code= self.cleaned_data.get('postal_code')
            gender= self.cleaned_data.get('gender')
            date_of_birth= self.cleaned_data.get('date_of_birth')
            
            models.SeekerPersonal.objects.create(
                user  = our_user,            
                country  = country,
                district = district,
                thana = thana,
                address = address,
                postal_code = postal_code,
                gender = gender,
                date_of_birth = date_of_birth,
            )
            print(our_user)
        return our_user
    
class SeekerUpdateForm(UserChangeForm):
    contact_no = forms.CharField()
    education_level= forms.ChoiceField( choices=constants.EDUCATION)
    board= forms.ChoiceField( choices=constants.BOARD)
    passing_year= forms.IntegerField()
    result = forms.CharField()
    group= forms.CharField()
    skillset= forms.CharField()
    experience= forms.CharField()
    
    
    country= forms.CharField()
    district= forms.CharField()
    thana= forms.CharField()
    address= forms.CharField()
    postal_code= forms.CharField()
    gender= forms.ChoiceField( choices= constants.GENDER)
    date_of_birth= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model= models.User
        fields = ['username','first_name', 'last_name', 'email', 'contact_no','gender','date_of_birth', 'education_level', 'board', 'passing_year', 'result', 'group', 'skillset', 'experience', 'district', 'thana', 'country','postal_code','address']
        exclude=['password']
        
        def __init__(self, *args: Any, **kwargs) :
            self.fields['password'].disabled = True 
            super().__init__(*args, **kwargs)
     
    def save(self, commit=True):
        our_user= super().save(commit=False)
        if commit:
            our_user.save()
            
            our_user_account, created= models.Seeker.objects.get_or_create(user=our_user)
            our_user_detail, created= models.SeekerPersonal.objects.get_or_create(user=our_user)
            
            our_user_account.contact_no=self.cleaned_data.get('contact_no') 
            our_user_account.education_level=self.cleaned_data.get('education_level') 
            our_user_account.board=self.cleaned_data.get('board')
            our_user_account.passing_year=self.cleaned_data.get('passing_year') 
            our_user_account.result=self.cleaned_data.get('result') 
            our_user_account.group=self.cleaned_data.get('group')
            our_user_account.skillset=self.cleaned_data.get('skillset') 
            our_user_account.experience=self.cleaned_data.get('experience')
        
            our_user_account.save()
            
            our_user_detail.country= self.cleaned_data.get('country')
            our_user_detail.district= self.cleaned_data.get('district')
            our_user_detail.thana= self.cleaned_data.get('thana')
            our_user_detail.address= self.cleaned_data.get('address')
            our_user_detail.postal_code= self.cleaned_data.get('postal_code')
            our_user_detail.gender= self.cleaned_data.get('gender')
            our_user_detail.date_of_birth= self.cleaned_data.get('date_of_birth')
            
            our_user_detail.save()
            
        return our_user
            
            
            
            