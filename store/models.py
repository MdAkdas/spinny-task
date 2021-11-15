from django.db import models

# Create your models here.
class Box(models.Model):
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
        self.area = 2*(l*b * + b*h + h*b)
        self.volume = l*b*h
        super(Box, self).save(*args, **kwargs) # Call the "real" save() method.