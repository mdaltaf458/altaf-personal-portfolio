from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    image = models.ImageField(upload_to='blog/images',null=True,blank=True)
    description=models.CharField(max_length=400)

    def __str__(self):                             #This function will display title of Blog we add directly in admin (browser) instead of blog object(1)
        return self.title
