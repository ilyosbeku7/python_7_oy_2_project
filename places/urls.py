from django.urls import path
from .views import PlacesView, AboutView

app_name='places'

urlpatterns=[
    path('places_page/', PlacesView.as_view(), name='places_page' ),
    path('about_page/<int:id>', AboutView.as_view(), name='about_page' )
]