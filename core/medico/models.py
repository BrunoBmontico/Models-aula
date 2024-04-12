from django.db import models

class Medico(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=2)
    phone = models.CharField(max_length=20)
