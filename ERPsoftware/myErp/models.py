from django.db import models

# Create your models here.
class UOMmaster(models.Model):
    unit = models.CharField(max_length=10,default=None)
    fullform = models.CharField(max_length=100,default=None)
    def __str__(self):
        return f"{self.unit}-{self.fullform}"
    
class State(models.Model):
    state = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.state}"