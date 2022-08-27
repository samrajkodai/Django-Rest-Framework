from http.client import HTTPException
from django.forms.models import model_to_dict
from django.http import JsonResponse
from . models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

@api_view(['POST'])
def api_home(request,*args, **kwargs):
    data=request.data
    
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        data=serializer.save()
        print("serializer.data",serializer.data)
        data=serializer.data
    else:
        print("invalid")
    return Response(data)