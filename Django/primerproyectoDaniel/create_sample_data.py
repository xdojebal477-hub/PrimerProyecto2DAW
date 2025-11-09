import os
import django

a=os.path.dirname(__file__)
# Ensure this script runs from project root where manage.py is
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primerpoyecto.settings')

# Setup Django
django.setup()

from blog.models import Autor, Post

print('Posts:', Post.objects.count())
print('Autores:', Autor.objects.count())

if Autor.objects.count() == 0:
    a = Autor.objects.create(nombre='AutorPrueba', email='autorprueba@example.com')
    print('Creado Autor:', a)
else:
    a = Autor.objects.first()

if Post.objects.count() == 0:
    p = Post.objects.create(titulo='Post de prueba', autor=a, cuerpo='Contenido de prueba', email='user@user.es')
    print('Creado Post:', p)

print('\nAhora visita:')
print('  /blog/ -> listado de posts')
print('  /blog/autores -> listado de autores')
