from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class timeSheetEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    time = models.IntegerField()
    comment = models.TextField()
    completed = models.BooleanField()
