from django.db import models

# Create your models here.
class intercambiador(Model.models):
    Email = models.EmailField(max_length=50,unique = True)
    Dni = models.CharField(min_length = 8,unique = True)
    Fnac = models.DateField

class ayudante(Model.models):
    Email = models.EmailField(max_length=50,unique = True)
    Dni = models.CharField(min_length = 8,unique = True)
    Fnac = models.DateField

