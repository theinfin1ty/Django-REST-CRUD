from rest_framework import serializers
from CRUD_APIs.models import Hero

class HeroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hero
    fields = ('id', 'name', 'alias')