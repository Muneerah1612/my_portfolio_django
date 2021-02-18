from django.db import models

# Create your models here.
class Project(models.Model):
    ''' add fields you want the database table to contain '''
    image = models.ImageField(upload_to = 'images')
    
    technology = models.CharField(max_length=40)
    about = models.CharField(max_length=255)

    def __str__(self):
        ''' this method returns a string representation of about text'''
        return self.about
