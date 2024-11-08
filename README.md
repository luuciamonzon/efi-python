## EFI - PYTHON
Este proyecto tiene como objetivo crear una API sobre la base de los modelos de un proyecto que consiste en el desarrollo de una aplicación web para gestionar un local de venta de celulares. La API debe permitir: Login
y creacion de usuarios, endpoints para obtener los objetos de todos los modelos (sin restriccion), endpoint para poder crear un objeto nuevo (limitado a usuarios admin), documentacion de los enpoints y al menos un modelo debe contener otro anidado.
La implementación se realiza usando Marshmallow para serialización y validación de datos.


## TECNOLOGÍAS UTILIZADAS:

- **Python**: Lenguaje de programación principal utilizado para desarrollar el proyecto.
- **Flask**: Framework ligero para el desarrollo de aplicaciones web.
- **Flask-SQLAlchemy**: ORM (Object Relational Mapper) que permite interactuar con la base de datos mediante objetos de Python en lugar de consultas SQL.
- **Flask-Migrate**: Herramienta que facilita la gestión de migraciones de bases de datos con `Alembic`, permitiendo realizar cambios estructurales sin pérdida de datos.
- **HTML/CSS**: Utilizados para construir la interfaz de usuario, donde HTML define el contenido y CSS el estilo visual de la aplicación.


## INSTALACIÓN:

Clonar el repositorio:  
`git clone git@github.com:luuciamonzon/efi-python.git`  

Crear un entorno virtual:  
`python3 -m venv env`  
`source env/bin/activate`  

Instalar dependencias:  
`pip install -r requirements.txt`  

Crear una base de datos (con el entotno activado):  
`sudo /opt/lampp/lampp start `  
`flask db init `// Solo la primera vez para configurar las migraciones  
`flask db migrate -m "Nombre de la migracion"` // Genera el archivo de migración con los cambios detectados en los modelos  
`flask db upgrade` // Para subir los cambios a la base de datos  

Correr el programa:  
`flask run`  
`flask run --reload` // no hay que parar flask con cada modificacion que se hace  






