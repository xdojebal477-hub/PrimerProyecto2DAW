from django.db import models

# Create your models here.
# class CategoriaChoices(models.TextChoices):
#     LEGUMBRE = 'LE', 'Legumbres'

class CategoriaIngrediente(models.Model):
    nombre=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} "

class Ingrediente(models.Model):
    nombre=models.CharField(max_length=100)
    categoria=models(CategoriaIngrediente, on_delete=models.CASCADE)