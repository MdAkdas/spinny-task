from django.db import models
from django.contrib.auth.models import User

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
        l = self.length 
        b = self.breadth
        h = self.height
        print()
        self.area = 2*(l*b * + b*h + h*b)
        self.volume = l*b*h
        super(Box, self).save(*args, **kwargs) # Call the "real" save() method.