from django.contrib import admin
from .models import User, FriendsRequest
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'phone_number')
    list_display_links=('id', 'username', )
    search_fields=('username', 'phone_number')

class FriendsRequestadmin(admin.ModelAdmin):
    list_display=('id', 'from_user', 'to_user')
    list_display_links=('id', 'from_user', )
   

admin.site.register(User, UserAdmin)
admin.site.register(FriendsRequest, FriendsRequestadmin)

