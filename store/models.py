from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Sum
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

# Create your models here.
class Box(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null = True)
    length  = models.IntegerField()
    breadth = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null = True)
    area = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        total_boxes = Box.objects.all().count()
        area_sum = Box.objects.all().aggregate(Sum('area'))['area__sum']
        volume_sum = Box.objects.all().aggregate(Sum('volume'))['volume__sum']

        print('total_boxes ', total_boxes)
        print('area_area ',area_sum)
        print('volume_volume ',volume_sum)

        l = self.length 
        b = self.breadth
        h = self.height

        curr_box_area = 2*(l*b * + b*h + h*b)
        curr_box_volume = l*b*h

        average_area = (area_sum + curr_box_area)/(total_boxes+1);
        average_volume = (volume_sum + curr_box_volume)/ (total_boxes+1)

        if average_area > 100:
            return Response({
                "message":"You are not the creator of the box. you cann't delete it."
            },
            status=status.HTTP_204_NO_CONTENT)
        elif average_volume > 100:
            return Response({
                "message":"You are not the creator of the box. you cann't delete it."
            },
            status=status.HTTP_204_NO_CONTENT)
        self.area = curr_box_area
        self.volume = curr_box_volume
        super(Box, self).save(*args, **kwargs) 