from rest_framework import generics
from rest_framework.response import Response
from .serializer import BoxSerializer
from .models import Box
from rest_framework.permissions import IsAuthenticated


class BoxListApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxCreateApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxDeleteApi(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer