from rest_framework.views import APIView
from . models import APIModel
from .serializers import APISerializers
from rest_framework.response import Response
from rest_framework import status


class TransformerList(APIView):
    """
    List all Transformers, or create a new Transformer
    """

    def get(self,request):
        transformers = APIModel.objects.all()
        serializer = APISerializers(transformers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
            serializer = APISerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MainView(APIView):

    def get(self, request, pk, format=None):
        data=APIModel.objects.get(pk=pk)
        serializer = APISerializers(data)
        return Response(serializer.data)

    def put(self,request,pk):
    
        print(request.data)
        user_data=APIModel.objects.get(pk=pk)
        serializer = APISerializers(user_data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk):
        try:
            data=APIModel.objects.get(pk=pk)
            data.delete()
            return Response({"Response":"Deleted successfully "})
        
        except:    
            return Response({"Requested data not found unable to delete"})




