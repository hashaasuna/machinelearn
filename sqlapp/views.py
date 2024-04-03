
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Psterminalinfo
from . import models
from funcs import serializers

@api_view(['GET'])
def getTerminalInfo(request):
    terminalinfo = Psterminalinfo.objects.all()[:10]
    serializer = serializers.ItemSerializer(terminalinfo, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getSales(request):
    sales = models.Pssales.objects.all()[:1]
    serializer = serializers.ItemSerializerSales(sales, many = True)
    return Response(serializer.data)

def index(request):
    return render(request, 'index.html')

# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Psterminalinfo
from . import models
from funcs import serializers

@api_view(['GET'])
def getTerminalInfo(request):
    terminalinfo = Psterminalinfo.objects.all()[:10]
    serializer = serializers.ItemSerializer(terminalinfo, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getSales(request):
    sales = models.Pssales.objects.all()[:1]
    serializer = serializers.ItemSerializerSales(sales, many = True)
    return Response(serializer.data)

def index(request):
    return render(request, 'index.html')

# Create your views here.
