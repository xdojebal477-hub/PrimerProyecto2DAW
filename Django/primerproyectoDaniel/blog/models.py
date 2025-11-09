from django.db import models

# Create your models here.
class Post(models.Model):
        titulo=models.CharField(max_length=200)
        autor=models.ForeignKey('Autor', on_delete=models.CASCADE, related_name='posts')
        cuerpo=models.TextField()
        email=models.EmailField(default='user@user.es')
        
        def  __str__(self):
            return self.titulo
        def resumen(self):
            return self.cuerpo[:50]+'...'

class Autor(models.Model):
        nombre=models.CharField(max_length=100)
        email=models.EmailField(unique=True)
        
        def __str__(self):
            return self.nombre