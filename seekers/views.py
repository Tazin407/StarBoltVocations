from django.shortcuts import render, redirect
from django.views.generic import CreateView,View,DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .import models
from django.views.generic import ListView
from .import models
from job.models import Job,Category, ApplyJob
from django.http import HttpResponse 
from .import forms
from django.urls import reverse_lazy
# Create your views here.

class SeekerRegister(CreateView):
    form_class= forms.SeekerRegistration
    template_name= 'all_forms.html'
    success_url= reverse_lazy('seeker_login')
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['type']= 'seeker'
        return context
    
class SeekerLogin(LoginView):
    template_name='all_forms.html'
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['type']= 'seeker'
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('seeker_profile')
    
    
    
class SeekerJobView(ListView):
    model= Job
    template_name="show_job_seeker.html"
    
    def get_queryset(self) :
        queryset= Job.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        category= Category.objects.all()
        context['category']=  category
        return context
    
def JobFilter(request, id):
    category= Category.objects.get(id=id)
    jobs= Job.objects.filter(category= category)
    all_category= Category.objects.all()
    
    
    return render(request, 'show_job_seeker.html', {'job_list':jobs,'category': all_category})
    
    

    
    
    
class ProfileView(View):
    template_name = 'seeker_profile.html'
    
    def get(self, request):
        try:
            seeker = models.Seeker.objects.get(user=request.user)
            form = forms.SeekerUpdateForm(instance=seeker)
        except models.Seeker.DoesNotExist:
            seeker = None
            form = forms.SeekerUpdateForm()
        
        return render(request, self.template_name, {'form': form, 'seeker': seeker})
    
    def post(self, request):
        try:
            seeker = models.Seeker.objects.get(user=request.user)
            form = forms.SeekerUpdateForm(request.POST, instance=seeker)
        except models.Seeker.DoesNotExist:
            seeker = None
            form = forms.SeekerUpdateForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('seeker_profile')
        
        return render(request, self.template_name, {'form': form, 'seeker': seeker})
    
class Show_Applied_Jobs(ListView):
    model= Job
    template_name= 'show_applied_jobs.html'
    context_object_name= 'job_list'
    
    def get_queryset(self):
        seeker= models.Seeker.objects.get(user= self.request.user)
        candidate_jobs = ApplyJob.objects.filter(candidate=seeker)
        queryset = [apply_job.job for apply_job in candidate_jobs]
        return queryset
    
    
def logout(request):
    logout(request)
    return redirect('home')





