from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import UpdateView



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    

    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request, 'users/profile_update.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request,'Profile update qilindi')
            return redirect('places:places_page')  
        return render(request, 'users/profile_update.html', {'form': form})

class ProfileView( LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, 'users/profile.html')
      

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
            return redirect('base')
        
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
                messages.success(request,'Tizimga muvafaqiyatli kirdingiz')
                return redirect('landing')
            
        return render(request, 'users/login_page.html' ,context={'form':form})
    
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):

        logout(request)
        messages.success(request,'Tizimdan muvafaqiyatli chiqish qildingiz ')
        return redirect( 'landing')