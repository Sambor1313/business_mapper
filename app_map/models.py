from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Proces(models.Model):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=2000)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 
       'Only alphanumeric characters are allowed.')
    color = models.CharField(max_length=6, 
                             default='CCCCCC', 
                             validators=[alphanumeric])