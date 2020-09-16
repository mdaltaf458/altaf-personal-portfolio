from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='portfolio/images')
    url=models. URLField(blank=True)

    def __str__(self):                             #This function will display title of project we add directly in admin (browser) insaed of project object(1)
        return self.title


