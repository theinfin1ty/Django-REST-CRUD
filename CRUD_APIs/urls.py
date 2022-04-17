from django.urls import path
from .views import *

app_name = 'CRUD_APIs'

urlpatterns = [
  path('heroes/', HeroView.as_view(), name='heroes'),
  path('heroes/<int:id>', OneHeroView.as_view(), name='heroesone'),
]