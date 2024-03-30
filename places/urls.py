from django.urls import path
from .views import PlacesView, AboutView,AddComment, landingPage

app_name='places'

urlpatterns=[
    path('places_page/', PlacesView.as_view(), name='places_page' ),
    path('about_page/<int:id>', AboutView.as_view(), name='about_page' ),
    path('add_comment/<int:id>', AddComment.as_view(), name='add_comment' ),
    path('home_page/', landingPage.as_view(), name='home' )
]