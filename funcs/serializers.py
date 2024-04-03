from rest_framework import serializers
from sqlapp.models import Psterminalinfo
from sqlapp import models

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psterminalinfo
        fields = '__all__'

class ItemSerializerSales(serializers.ModelSerializer):
    class Meta:
        model = models.Pssales
        fields = '__all__'