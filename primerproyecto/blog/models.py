from django.db import models

# Create your models here.
class Post(models.Model):
    titulo=models.CharField(max_length=200)
    autor=models.ForeignKey(to='Autor')
    cuerpo=models.TextField()
    email=models.EmailField(default='dani@gmail.com')

    
    def __str__(self):
        return f"({self.id}){self.titulo}"


class Autor(models.Model):
    nombre=models.CharField(max_length=200)
    edad=models.TextField()

    def __str__(self):
        return f"({self.id}) {self.nombre}"