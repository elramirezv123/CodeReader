CodeReader APP
===============
Instrucciones de instalación
----------------------------
1.	Instalar `python 3.6.8` para poder correr la aplicación. Descargar en https://www.python.org/downloads/release/python-368/

2.	**(Windows)** Iniciando la instalación, se desplegará en pantalla la opción de agregar `python` al PATH (para poder utilizarlo en la terminal), hay que darle OK para que se agregue automáticamente a las variables de entorno.

3.	Luego de instalar `python 3.6.8`, se deben instalar algunas líbrerias adicionales. Para ello, se debe abrir la terminal (Sìmbolo del sistema) y correr el comando `python -m pip install -r requirements.txt`. Debería aparecer un mensaje de diciendo que la instalación fue exitosa.

Instrucciones de uso
--------------------
1.	Dentro de la carpeta del programa correr en la terminal el comando `python main.py`
2. Se deberá desplegar el software en toda la pantalla y ya estará listo para su uso.

Preguntas frecuentes
---------
#### ¿Puedo cargar mi propia base de datos?
**R**: Sí, se debe guardar en la carpeta del programa con el nombre `db.json`. Cabe mencionar que este archivo debe tener un formato predeterminado para que pueda ser leído correctamente. Puede ser del largo que sea necesario.
```
[
    {  
        "Nombre": "Cuaderno azul largo 100 hjs",
        "Marca": "Auca",
        "Precio": "580",
        "Codigo": "780605935341",
        "Imagen": "assets/caz.jpg",
        "Cantidad": "6"
    },
    {
        "Nombre": "Plumon Super color marker negro",
        "Marca": "Pilot",
        "Precio": "890",
        "Codigo": "4902505087578",
        "Imagen": "",
        "Cantidad": "10"
    }
]
```
