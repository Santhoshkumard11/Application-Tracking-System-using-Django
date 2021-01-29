from django.db import models

# Create your models here.


class Profile(models.Model):

    name = models.CharField(max_length=50)

    address = models.TextField(max_length=100)
    
    #dob

    def __str__(self):

        return self.name
