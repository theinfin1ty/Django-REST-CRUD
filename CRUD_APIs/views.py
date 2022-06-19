from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HeroSerializer
from .models import Hero
# Create your views here.

class HeroView(APIView):
  def get(self, request):
    heroes = Hero.objects.all()
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = HeroSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OneHeroView(APIView):
  def get(self, request, id):
    heroes = Hero.objects.filter(id = id)
    serializer = HeroSerializer(heroes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def patch(self, request, id):
    heroes = Hero.objects.get(id = id)
    serializer = HeroSerializer(heroes, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  

  