from places.models import Place, Comment
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import PlaceSerializer,  CommentSerializer
from django.shortcuts import get_object_or_404

class PlaceApiView(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class PlaceDetailApiView(APIView):
     def get(self, request, id):
        place =get_object_or_404(Place,id=id)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    
class ReviewsApiView(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Result":"Success"})