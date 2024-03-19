from django.urls import path
from .views import RegisterView, LoginView

app_name='users'

urlpatterns = [
    
    path('register_page/', RegisterView.as_view(), name='register_page'), 
    path('login_page/', LoginView.as_view(), name='login_page'), 
]
