[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HE5JzsYK)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21063033&assignment_repo_type=AssignmentRepo)
# bibliotecamusical

### Gestión de una playlist musical con usuarios, favoritos y almacenamiento en JSON

---

## Descripción general

Se desea desarrollar un programa en **Python** que gestione la información de una **plataforma musical**.
El sistema deberá manejar **dos tipos de datos principales**, ambos almacenados en **ficheros JSON**:

1. **Canciones**
2. **Usuarios**

Cada usuario incluirá un **diccionario anidado** con sus canciones favoritas y valoraciones personales.

---

## Estructuras de datos

### 1. Diccionario de canciones

Cada canción estará representada mediante un diccionario con la siguiente estructura:

```python
{
    "id": int,               # Identificador único de la canción
    "titulo": str,
    "artista": str,
    "anio": int,
    "genero": str
}
```

Todas las canciones se almacenarán en una lista llamada `canciones`,
y se guardarán en el fichero **`canciones.json`**.

---

### 2. Diccionario de usuarios

Cada usuario se representará mediante un diccionario con esta estructura:

```python
{
    "nombre_usuario": str,
    "edad": int,
    "pais": str,
    "favoritos": {           # Diccionario anidado
        "id_cancion": valoracion_float,
        ...
    }
}
```

* En `favoritos`, las **claves** son los identificadores (`id`) de canciones,
  y los **valores** son las **valoraciones personales** (de 0.0 a 10.0).
* Todos los usuarios se almacenarán en una lista llamada `usuarios`,
  guardada en **`usuarios.json`**.

---

## Requisitos del programa

### 1. Carga y guardado de información

* Al iniciar el programa:

  * Se deben cargar automáticamente los datos de los ficheros `canciones.json` y `usuarios.json`.
  * Si alguno no existe, el programa debe crear listas vacías por defecto.
* Al salir del programa:

  * Se deben **guardar los datos actualizados** en los mismos ficheros, en formato JSON legible (`indent=4`).

> Se recomienda usar las funciones `json.load()` y `json.dump()` del módulo estándar `json`.

---

### 2. Menú principal

El programa mostrará un menú de usuario con las siguientes opciones:

```
1. Mostrar todas las canciones
2. Añadir nueva canción
3. Buscar canciones por título o artista
4. Registrar nuevo usuario
5. Añadir canción a favoritos de un usuario
6. Mostrar canciones favoritas de un usuario
7. Filtrar canciones por género o año
8. Mostrar estadísticas (valoraciones y popularidad)
9. Guardar y salir
```

El menú se repetirá hasta que el usuario elija la opción **9**.

---

## Detalles funcionales de las operaciones

### Mostrar canciones

Listar todas las canciones con su información formateada.

### Añadir nueva canción

Solicitar los datos de la canción al usuario y asignar un `id` único (por ejemplo, el mayor existente + 1).

### Buscar canciones

Permitir buscar por título o artista (sin distinguir mayúsculas/minúsculas) y mostrar los resultados.

### Registrar usuario

Solicitar datos básicos del usuario y añadirlo a la lista `usuarios`.

### Añadir canción a favoritos

Solicitar el nombre de usuario y el ID de la canción.
Pedir una valoración (0–10) y añadirla al diccionario `favoritos` del usuario.
Si ya existe, actualizar la valoración.

### Mostrar canciones favoritas

Mostrar el listado de canciones favoritas de un usuario junto con sus valoraciones.

### Filtrar canciones

Permitir filtrar por **género** o por **año** y mostrar las coincidencias.

### Estadísticas

Calcular y mostrar:

* La **media general** de las valoraciones de todos los usuarios.
* La **canción mejor valorada**.
* La **canción más popular** (la que aparece más veces en favoritos).

---


## Puntuación orientativa

| Criterio                                                            | Puntos        |
| ------------------------------------------------------------------- | ------------- |
| Carga y guardado en ficheros JSON                                   | 2             |
| Uso de listas y diccionarios anidados                               | 2             |
| Implementación del menú y validaciones                              | 2             |
| Operaciones avanzadas (búsqueda, filtrado, estadísticas, favoritos) | 3             |
| Claridad, organización y documentación del código                   | 1             |
| **Total**                                                           | **10 puntos** |


