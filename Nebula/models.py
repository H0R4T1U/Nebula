from django.db import models



class Project(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    language = models.CharField(max_length=200, null=True)
    stars = models.IntegerField()

