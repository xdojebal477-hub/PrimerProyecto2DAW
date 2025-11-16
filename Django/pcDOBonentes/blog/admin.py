from django.contrib import admin
from.models import Cliente, PC, Producto, CPU, RAM, SSD, GPU
# Register your models here.
admin.site.register(Cliente)
admin.site.register(PC)
#admin.site.register(Producto) # Puedes registrar la base si quieres
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(SSD)
admin.site.register(GPU)
