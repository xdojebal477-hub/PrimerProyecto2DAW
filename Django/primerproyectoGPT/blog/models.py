from django.db import models

# Create your models here.
class Post(models.Model):
        titulo=models.CharField(max_length=200)
        autor=models.CharField(max_length=200)
        cuerpo=models.TextField()
        email=models.EmailField(default='user@user.es')
        
        def  __str__(self):
            return self.titulo
        def resumen(self):
            return self.cuerpo[:50]+'...'

