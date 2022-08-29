from rest_framework.views import APIView
from rest_framework import mixins
from . models import APIModel
from . serializers import APISerializers
from rest_framework import generics

class TransformerList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

        queryset = APIModel.objects.all()
        serializer_class = APISerializers

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)


        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)


class MainView(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

        queryset = APIModel.objects.all()
        serializer_class = APISerializers

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)


