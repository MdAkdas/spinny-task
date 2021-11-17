from rest_framework import generics
from rest_framework.response import Response
from .serializer import BoxSerializer
from .models import Box
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status


class BoxListApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Box.objects.all()

    serializer_class = BoxSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'length':['gt', 'lt'],
        'breadth':['gt', 'lt'],
        'height':['gt', 'lt'],
        'area':['gt', 'lt'],
        'volume':['gt', 'lt'],
        'user__username': ['exact'],
        'created_at': ['lt','gt']
    }



class MyBoxListApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BoxSerializer
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        user = self.request.user
        return Box.objects.filter(user=user)
    
    filterset_fields = {
        'length':['gt', 'lt'],
        'breadth':['gt', 'lt'],
        'height':['gt', 'lt'],
        'area':['gt', 'lt'],
        'volume':['gt', 'lt'],
    }
    

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id == self.request.user.id:
            self.perform_destroy(instance)
            return Response({
                "message":"Box deleted successfully"
            },
            status=status.HTTP_200_OK)
        else:
            return Response({
                "message":"You are not the creator of the box. you cann't delete it."
            },
            status=status.HTTP_204_NO_CONTENT)