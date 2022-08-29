from email.policy import HTTP
from http.client import HTTPException
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import APISerializers
from django.http import JsonResponse
from rest_framework.response import Response
from .models import APIModel
from rest_framework import status



@api_view(['POST'])

def create(request):

    serializer=APISerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response({"Response":"Invalid Credentials"})



@api_view(['GET'])

def get_one(request,pk):

    data=APIModel.objects.get(pk=pk)

    serializer=APISerializers(data)

    # if serializer.is_valid():
        
    return Response(serializer.data,status=status.HTTP_200_OK)

  


@api_view(['PUT'])

def update(request,pk):

    data=APIModel.objects.get(pk=pk)

    serializer=APISerializers(data,request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response({"Response":"Invalid Credentials"})



@api_view(['DELETE'])

def delete(request,pk):

    try:
        data=APIModel.objects.get(pk=pk)
        data.delete()
        return Response({"Response":"Deleted successfully "})
    
    except:    
        return Response({"Requested data not found unable to delete"})
   