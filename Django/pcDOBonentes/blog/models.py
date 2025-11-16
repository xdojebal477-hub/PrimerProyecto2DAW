from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField( max_length=50)
    email = models.EmailField(blank=True, null=True)
    
    def ver_Pcs(self):
        return self.pcs.all()
    def __str__(self):
        return self.nombre

class PC(models.Model):
    nombre=models.CharField( max_length=50,unique=True)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name='pcs')
    cpu=models.ForeignKey('CPU',on_delete=models.CASCADE)
    ram=models.ForeignKey('RAM',on_delete=models.CASCADE)
    ssd=models.ForeignKey('SSD',on_delete=models.CASCADE)
    gpu=models.ForeignKey('GPU',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'PC {self.nombre}:\n - CPU:{self.cpu} \n - RAM:{self.ram} \n - SSD:{self.ssd} \n - GPU:{self.gpu}'






class Producto(models.Model):
    nombre=models.CharField( max_length=50,unique=True)
    precio=models.IntegerField(default=0)
    especificacion=models.CharField(max_length=500)
    
    def __str__(self):
        return f'{self.nombre} \n {self.especificacion} \n {self.precio}'

class CPU(Producto):
    pass
class RAM(Producto):
    pass

class SSD(Producto):
    pass

class GPU(Producto):
    pass