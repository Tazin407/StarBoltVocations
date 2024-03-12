from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from .import models
from .import forms
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth import login, logout, update_session_auth_hash
from django.http import Http404, HttpRequest, HttpResponse
from job.models import Job, Category
# Create your views here.

class EmpRegister(CreateView):
    form_class= forms.EmployerRegistration
    template_name= 'all_forms.html'
    success_url= reverse_lazy('employer_login')
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['type']= 'employer'
        context['purpose']= 'Sign Up'
        return context
    
class EmployerLogin(LoginView):
    template_name='all_forms.html'
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['type']= 'employer'
        context['purpose']= 'Log In'
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('employer_profile')
    

class EmpProfileView(View, LoginRequiredMixin):
    template_name= 'employer_profile.html'
    
    def get(self, request):
        
        try:
            emp= models.Employer.objects.get(user= request.user)
            form= forms.EmployerUpdateForm(instance= emp)
            return render(request, self.template_name, {"form":form})
        except models.Employer.DoesNotExist:
            raise Http404('Account does not exist')
    
    def post(self, request):
        form= forms.EmployerUpdateForm(request.POST, instance= request.user)
        
        if form.is_valid():
            form.save()
            return redirect('employer_profile')
        
        return render(request, self.template_name, {'form': form})    


def Emplogout(request):
    logout(request)
    return redirect('home')



#added later

class EmpJobView(ListView):
    model= Job
    template_name="show_job_employer.html"
    
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
    print(jobs)
    
    return render(request, 'show_job_employer.html', {'job_list':jobs,'category': all_category})