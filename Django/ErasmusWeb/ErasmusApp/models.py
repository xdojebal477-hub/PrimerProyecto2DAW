from django.db import models

# Create your models here.
class Sexo(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    OTRO = 'O', 'Otro'  # Opcional, por si acaso

    
class Persona(models.Model):
    
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    clase = models.CharField(max_length=50, verbose_name="Clase")
    # Opciones para sexo (según documento)
    sexo = models.CharField(
            max_length=1, 
            choices=Sexo.choices, 
            default=Sexo.MASCULINO,
            verbose_name="Sexo"
        )
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    numero_pasaporte = models.CharField(max_length=50, verbose_name="Nº Pasaporte/DNI")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    
    # --- 2. CONTACTO ---
    telefono_privado = models.CharField(max_length=20, blank=True, null=True)
    movil = models.CharField(max_length=20, verbose_name="Móvil")
    email_alumno = models.EmailField(verbose_name="Email del alumno")
    email_padres = models.EmailField(verbose_name="Email de los padres")
    
    # --- 3. FAMILIA ---
    profesion_padre = models.CharField(max_length=100, blank=True, null=True)
    profesion_madre = models.CharField(max_length=100, blank=True, null=True)
    edad_hermanos = models.CharField(max_length=50, blank=True, null=True, help_text="Ej: 12, 15")
    edad_hermanas = models.CharField(max_length=50, blank=True, null=True, help_text="Ej: 10")
    mascotas = models.CharField(max_length=200, blank=True, null=True, verbose_name="Mascotas (¿cuáles?)")
    
    # --- 4. SALUD Y OTROS ---
    problemas_salud = models.TextField(blank=True, null=True, verbose_name="Problemas de salud (alergias, etc.)")
    es_vegetariano = models.BooleanField(default=False, verbose_name="Soy vegetarian@")
        # Preferencias de intercambio (Radio Buttons en el word)
    
    class PreferenciaGenero(models.TextChoices):
        CHICO = 'CHICO', 'Un chico'
        CHICA = 'CHICA', 'Una chica'
        DA_IGUAL = 'DA_IGUAL', 'Da igual'
    
    preferencia_intercambio = models.CharField(max_length=10,choices=PreferenciaGenero.choices,default=PreferenciaGenero.DA_IGUAL,verbose_name="Como intercambio prefiero"
    )
    
    puedo_alojar_dos = models.BooleanField(default=False, verbose_name="Puedo alojar a dos alumnos")
    interes_larga_duracion = models.BooleanField(default=False, verbose_name="Quisiera participar en larga duración (4º ESO)")

    # --- 5. PERFIL (Carácter, Deportes, etc.) ---
    caracter = models.TextField(blank=True, verbose_name="Carácter (descríbete brevemente)")
    deportes = models.TextField(blank=True, verbose_name="Mis deportes")
    musica = models.TextField(blank=True, verbose_name="Música y grupos favoritos")
    otros_hobbies = models.TextField(blank=True, verbose_name="Otros pasatiempos (leer, cine, etc.)")

    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"