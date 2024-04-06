from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileForm, ResetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import UpdateView
from .models import User, FriendsRequest



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    

    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request, 'users/profile_update.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user, files=request.FILES)
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
                messages.success(request,'Tizimga muvafaqiyatli kirdingiz')
                return redirect('landing')
            
        return render(request, 'users/login_page.html' ,context={'form':form})
    
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):

        logout(request)
        messages.success(request,'Tizimdan muvafaqiyatli chiqish qildingiz ')
        return redirect( 'landing')

class ResetPasswordView(LoginRequiredMixin, View):

    def get(self, request):
        form=ResetPasswordForm()

        return render(request, 'users/reset_password.html' , {"form":form})
    
    def post(self, request):
        form=ResetPasswordForm(request.POST)
        user=request.user

        if form.is_valid():
            if check_parol(user, form.cleaned_data['old_password']):
                user.set_password(form.cleaned_data['confirm_password'])
                user.save()
                return redirect('users:login_page')
            else:
                return render(request, "users/reset_password.html", {'form':form})
        return render(request, "users/reset_password.html", {'form':form})
    
def check_parol(user, password):

    return user.check_password(password)

class UsersView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.exclude(username=request.user.username).exclude(friends=request.user)

        friend_requests = User.objects.filter(id__in=FriendsRequest.objects.filter(from_user=request.user).values_list('to_user'))



        return render(request, 'users/users.html', {"users": users, "friend_requests": friend_requests})


class MyNetworksView(LoginRequiredMixin, View):
    def get(self, request):
        networks = FriendsRequest.objects.filter(to_user=request.user, is_accepted=False)

        return render(request, 'users/networks_list.html', {"networks": networks})


class AcceptFriendRequestView(LoginRequiredMixin, View):
    def get(self, request, id):
        friend_request = FriendsRequest.objects.get(id=id)
        from_user = friend_request.from_user
        main_user = request.user

        main_user.friends.add(from_user)
        from_user.friends.add(main_user)

        friend_request.is_accepted = True
        friend_request.save()

        return redirect("users:networks")


class IgnoreFriendRequestView(LoginRequiredMixin, View):
    def get(self, request, id):
        friend_request = FriendsRequest.objects.get(id=id)
        friend_request.delete()
        return redirect("users:networks")


class DeleteFromFriendsView(LoginRequiredMixin, View):
    def get(self, request, id):
        friend = User.objects.get(id=id)
        user = request.user
        user.friends.remove(friend)
        friend.friends.remove(user)

        return redirect("users:networks")


class SendFriendRequestView(LoginRequiredMixin, View):
    def get(self, request, id):
        to_user = User.objects.get(id=id)
        from_user = request.user

        FriendsRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

        return redirect("users:users")


