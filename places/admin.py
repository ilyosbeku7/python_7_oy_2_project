from django.contrib import admin

from .models import Owner, PlaceOwner, Comment, Place

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'email')
    search_fields=('first_name', 'last_name', 'email')
    list_display_links=( 'first_name', )
    
class PlaceAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'address')
    search_fields=( 'name', )
    list_display_links=( 'name', )


class CommentAdmin(admin.ModelAdmin):
    list_display=('user', 'place', 'star_given')
    search_fields=( 'user', 'place', )
    list_display_links=( 'user', )

class PlaceOwnerAdmin(admin.ModelAdmin):
    list_display=('place', 'owner', )
    search_fields=( 'owner', 'place', )
    list_display_links=( 'place', )

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PlaceOwner, PlaceOwnerAdmin)
admin.site.register(Place, PlaceAdmin)