from django.shortcuts import render, get_object_or_404, redirect
from .models import Place, Owner, PlaceOwner, Comment
from django.views import View
from .forms import PlaceCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
# Create your views here.

class PlacesView(View):
    def get(self, request):
        
        places=Place.objects.all()
        search_query=request.GET.get('q', "")
        if search_query:
            places=places.filter(name__icontains=search_query,)
    
        data={
            
            'places':places
        }

        return render(request, 'places/places_page.html', context=data, )
    

class AboutView(View):

    def get(self, request, id):
        owners=PlaceOwner.objects.all()
        detail=get_object_or_404(Place, pk=id)
        comments=Comment.objects.all()
        form=PlaceCommentForm()  

        data={
            'owners':owners,
            'detail':detail,
            'form': form,
            'comments':comments
        }

        return render(request, 'places/about_page.html', context=data)
    
class AddComment(LoginRequiredMixin, View):
    def post(self, request, id):
        form = PlaceCommentForm(request.POST)
        place = Place.objects.get(id=id)
        data = {
            'form': form,
            'place': place
        }
        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                place=place,
                comment_text=form.cleaned_data['comment_text'],
                star_given=form.cleaned_data['star_given']
            )
            return redirect(reverse('places:about_page', kwargs={'id': place.id}))
        return render(request, 'places/about_page.html', context=data)

    
class landingPage( View):
    def get(self, request):
        
        comment = Comment.objects.all()
        reversed_comments = comment[::-1]  # Reverse the order of comments
        last_4_comments = reversed_comments[:4]
        data={
            
            'last_4_comments':last_4_comments
        }

        return render(request, 'places/home_page.html', context=data )
    