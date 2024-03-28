from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, ProfileUpdateView

app_name='users'

urlpatterns = [
    
    path('register_page/', RegisterView.as_view(), name='register_page'), 
    path('login_page/', LoginView.as_view(), name='login_page'), 
    path('logout_page/', LogoutView.as_view(), name='logout_page'), 
    path('profile/', ProfileView.as_view(), name='profile'), 
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'), 
]
