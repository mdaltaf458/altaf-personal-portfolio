from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    image = models.ImageField(upload_to='blog/images',null=True,blank=True)
    description=models.CharField(max_length=400)
