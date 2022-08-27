# from http.client import HTTPException
# from django.forms.models import model_to_dict
# from django.http import JsonResponse
# from . models import Product
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import ProductSerializer


# @api_view(['POST'])
# def api_home(request,*args, **kwargs):
#     data=request.data
    
#     serializer=ProductSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         data=serializer.save()
#         print("serializer.data",serializer.data)
#         data=serializer.data
   
#         return Response(data)

#     return Response({'invalid data'})


from rest_framework import generics
from . models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()

    serializer_class=ProductSerializer


