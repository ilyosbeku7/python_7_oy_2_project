from django.urls import path
from .views import RegisterView, LoginView, LogoutView, IgnoreFriendRequestView, DeleteFromFriendsView, ProfileView, ProfileUpdateView, AcceptFriendRequestView, MyNetworksView, ResetPasswordView, UsersView, SendFriendRequestView

app_name='users'

urlpatterns = [
    
    path('register_page/', RegisterView.as_view(), name='register_page'), 
    path('login_page/', LoginView.as_view(), name='login_page'), 
    path('logout-page/', LogoutView.as_view(), name='logout_page'), 
    path('profile/', ProfileView.as_view(), name='profile'), 
    path('profile_update/', ProfileUpdateView.as_view(), name='profile_update'), 
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'), 
    path('users/', UsersView.as_view(), name='users'), 


    path('send_request/<int:id>/', SendFriendRequestView.as_view(), name='send_request'), 
    path('networks/', MyNetworksView.as_view(), name='networks'), 
    path('accept_friends/<int:id>', AcceptFriendRequestView.as_view(), name='accept_friends'), 
    path('ignore-friend/<int:id>', IgnoreFriendRequestView.as_view(), name='ignore_friends'), 
    path('delete-friend/<int:id>', DeleteFromFriendsView.as_view(), name='delete_friends'), 
]
