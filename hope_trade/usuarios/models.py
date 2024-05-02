from django.db import models

# Create your models here.
class intercambiador(Model.models):
    Email = models.EmailField(max_length=50,unique = True)
    Dni = models.CharField(min_length = 8,unique = True)
    Fnac = models.DateField
    Clave = models.CharField(min_length = 6) 
    Estado = models.BooleanField(default=False) #Aca tomo solo dos valores, activo o suspendido, si se elimina tbn se elimina de la BD

class ayudante(Model.models):
    Email = models.EmailField(max_length=50,unique = True)
    Dni = models.CharField(min_length = 8,unique = True)
    Fnac = models.DateField
    Clave = models.CharField(min_length = 6) 
    Filial = ArrayField(models.CharField(max_length=50)) #chequear esta linea :) 
    

