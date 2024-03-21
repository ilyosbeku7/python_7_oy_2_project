from django.shortcuts import render, get_object_or_404
from .models import Place, Owner, PlaceOwner, Comment
from django.views import View

# Create your views here.

class PlacesView(View):
    def get(self, request):

        places=Place.objects.all()
    
        data={
            'places':places
        }

        return render(request, 'places/places_page.html', context=data)
    

class AboutView(View):

    def get(self, request, id):
        owners=PlaceOwner.objects.all()
        detail=get_object_or_404(Place, pk=id)
        comments=Comment.objects.all()
        

        data={
            'owners':owners,
            'detail':detail,
            
            'comments':comments
        }

        return render(request, 'places/about_page.html', context=data)
    
