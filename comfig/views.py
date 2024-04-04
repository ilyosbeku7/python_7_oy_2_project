from django.shortcuts import render
from places.models import Comment
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

def landing_page(request):
   return render (request, 'landing_page.html')


class HomeView(LoginRequiredMixin, View):
   def get(self, request):
      place_reviews=Comment.objects.exclude(user=request.user)
      return render (request, 'home.html', {"place_reviews":place_reviews})