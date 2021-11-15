from rest_framework import generics
from rest_framework.response import Response
from .serializer import BoxSerializer
from .models import Box


class BoxListApi(generics.ListAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxCreateApi(generics.CreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxDeleteApi(generics.DestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer