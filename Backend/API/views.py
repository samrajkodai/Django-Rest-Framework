from os import stat
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import APISerializers
from django.http import JsonResponse
from rest_framework.response import Response
from .models import APIModel
from rest_framework import status


@api_view(['GET'])

def create(request):
    return Response({"result":"post created successfully"})