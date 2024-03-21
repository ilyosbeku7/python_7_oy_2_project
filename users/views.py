from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class ProfileView(View):
    
        
        form_class=ProfileForm
        model=User
        template_name='users/profile.html'
        
        def get(self, request):
            users=User.objects.all()
            data={
            'users':users
                 }
            return render (request, 'users/profile.html', context=data)
        

      

# Create your views here.
class RegisterView(View):

    def get(self, request): 
        form=RegisterForm
        return render (request, 'users/register_page.html', context={'form':form})

    def post(self, request):
        form=RegisterForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('landing')
        
        return render (request, 'users/register_page.html', context={'form':form})

class LoginView(View):
    

    def get(self, request): 
        form=LoginForm
        return render (request, 'users/login_page.html', context={'form':form})

    def post(self, request):
        form=LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate( request, username=username, password=password)
           
        
            if user is not None:
                login(request, user)
                return redirect('landing')
            
        return render(request, 'users/login_page.html' ,context={'form':form})
    
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):

        logout(request)

        return redirect( 'landing')