from django.db import models

# Create your models here.
# class CategoriaChoices(models.TextChoices):
#     LEGUMBRE = 'LE', 'Legumbres'

class CategoriaIngrediente(models.Model):
    nombre=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} "

class Lactosa (models.Model):
    lactosa=models.BooleanField()

    def __str__(self):
        return f"{self.lactosa}"    

class Cantidad(models.Model):
    cantidad=models.IntegerField()
    def __str__(self):
        return f"{self.cantidad}" 

class Ingrediente(models.Model):
    nombre=models.CharField(max_length=100)
    categoria=models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE)
    lactosa=models.ForeignKey(Lactosa, on_delete=models.CASCADE,default=False)
    cantidad=models.ForeignKey(Cantidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - {self.lactosa} - {self.cantidad}"



class Recetas(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    ingredientes=models.ManyToManyField(Ingrediente,related_name='recetas')

    def __str__(self):
        return f"{self.nombre} : {self.descripcion} "