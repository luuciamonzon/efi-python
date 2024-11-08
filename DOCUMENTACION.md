## DOCUMENTACIÓN DE ENDPOINTS: 


#### NOTA GENERAL:
Todos los endpoints requieren que el usuario esté autenticado y tenga permisos de administrador para realizar acciones específicas. En caso de errores, se proporcionan mensajes claros que indican el problema.

#### LOGIN : 


##### MÉTODO POST / AUTENTICACIÓN
Endpoint : /login

Cuerpo de la solicitud: 
```json
    {
    "username":"nombre",
    "password":"contraseña"
    }
```
Respuesta: 
```json
    {
    "token":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."
    }
```

#### USERS: 


##### MÉTODO POST 

Endpoint : /users

Cuerpo de la solicitud: 
```json
    {
    "username":"luucia",
    "password" "monzon1"
    }
```
Respuesta:
```json 
{
  "Mensaje": "Usuario creado correctamente",
  "Usuario": {
    "username": "usuario nuevo",
    "is_admin": true
  }
}
```
Mensajes de error:  
    `403 Forbidden`: Solo los administradores pueden crear usuarios.  
    `500 Internal Server Error`: Fallo la creación del usuario.  
 

##### MÉTODO GET

Si el usuario autenticado es administrador, se devuelve la lista completa con detalles de cada usuario. Si el usuario no es administrador, se devuelve una versión minimalista de los datos del usuario.

##### MÉTODO DELETE

Endpoint : /users/ID del usuario a eliminar/delete

Respuesta:
```json
{
  "200 OK": "Usuario eliminado correctamente."
}
```
Mensajes de error:   
    `403 Forbidden`: Solo el admin pueden crear usuarios.  
    `404 Not found`:Usuario no encontrado.  
    `500 Internal Server Error`: Fallo al eliminar el usuario.  

##### MÉTODO PUT 

Endpoint : /users/ID del usuario a actualizar/update

Cuerpo de la solicitud: 
```json
    {
    "username":"dato a actualizar, si se desea",
    "password": "dato a actualizar, si se desea"
    }
```
Respuesta:
```json
{
  "200  OK": "Usuario actualizado correctamente."
}
```
Mensajes de error:   
    `403 Forbidden`: No tienes permiso para actualizar usuarios.  
    `404 Not found`:Usuario no encontrado.  
    `500 Internal Server Error`: Error al actualizar el usuario.  


#### MARCA: 


##### MÉTODO POST


Endpoint : /marca

Cuerpo de la solicitud: 
```json
    {
    "nombre":"Nombre de la marca a crear"
    }
```
Respuesta:
```json
"marcas":
    {
      "id": 1,
      "nombre": "Samsumg"
    }
```
Mensajes de error:   
    `403 Forbidden`: No está autorizado para crear marcas.  
    `403 Forbidden`: No está autorizado para editar marca.  
 


##### MÉTODO GET 


Endpoint : /marca

Respuesta: 
```json
{
  "marcas": [
    {
      "id": 1,
      "nombre": "Samsung"
    },
    {
      "id": 2,
      "nombre": "Apple"
    },
    {
      "id": 3,
      "nombre": "Motorola"
    },
    {
      "id": 4,
      "nombre": "Nokia"
    },
    {
      "id": 5,
      "nombre": "BlackBerry"
    }
  ]
}
```

#### STOCK: 

##### MÉTODO POST: 


Endpoint : /stock

Endpoint : /eliminar_stock

Respuesta:
```json
{
  "200  OK": "Stock restado correctamente."
}
```

Mensajes de error:   
    `400 Bad Request`: Debe proporcionar 'telefono_id' y 'cantidad'.  
    `400 Bad Request`: Cantidad debe ser un número entero.  
    `400 Bad Request`: Datos inválidos  
    `403 Forbidden`: No está autorizado para acceder a esta ruta.  
    `403 Forbidden`: No está autorizado para borrar stock.  
    

##### MÉTODO GET: 


Endpoint : /stock

Respuesta:
```json
[
  {
    "accesorios": [
      {
        "id": 1,
        "nombre": "Cargador Samsung"
      },
      {
        "id": 3,
        "nombre": "Funda Apple original"
      },
      ...
    ]
  }
]
```

#### ACCESORIOS: 

##### MÉTODO POST: 

Endpoint : /accesorios

Cuerpo de la solicitud: 
```json
    {
    "nombre":"Nombre del accesorio a crear"
    }
```
Respuesta: 
```json
    {
     "201 Created": "Accesorio creado exitosamente"
    }
```
Mensaje de error:
```json 
{
    "403 Forbidden": "No está autorizado para crear accesorio."
}
```
Endpoint : /accesorio/ID del accesorio a eliminar/eliminar

Respuesta: 
```json
{
  "200 OK":"Accesorio eliminado exitosamente."
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "No está autorizado para eliminar accesorio."
}
```
Endpoint : /accesorio/ID del accesorio a editar/editar

Respuesta: 
```json
{
  "200 OK":"Accesorio actualizado exitosamente"
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "No está autorizado para editar accesorio"
}
```


##### MÉTODO GET: 

Endpoint : /accesorios

Respuesta: 
```json
{
  "200 OK": {
    "accesorios": [
      {
        "id": 1,
        "nombre": "Cargador Samsung"
      },
      {
        "id": 3,
        "nombre": "Funda Apple original"
      },
      ...
    ]
  }
}
```

#### TIPO: 


##### MÉTODO POST: 
Endpoint : /tipo

Cuerpo de la solicitud: 
```json
    {
    "nombre":"tipo"
    }
```
Respuesta: 
```json
{
  "200": "Tipo creado exitosamente."
}
```
Endpoint: /tipo/ID del tipo a eliminar/eliminar

Respuesta: 
```json
{
  "200": "Tipo creado exitosamente."
}
```


Mensajes de error:   
    `403 Forbidden`: No está autorizado para crear tipos.    
    `403 Forbidden`: No está autorizado para eliminar tipos.    
    `404 Not Found`: Tipo no encontrado.    

##### MÉTODO GET: 
Endpoint : /tipo

Respuesta: 
```json
{
  "200 OK": {
    "tipos": [
      {
        "id": 1,
        "nombre": "Gama alta"
      },
      {
        "id": 3,
        "nombre": "Gama baja"
      },
      ...
    ]
  }
}
```

#### TELEFONO: 


##### MÉTODO POST: 


Endpoint: /telefono

Cuerpo de la solicitud: 
```json
    {
  "modelo": "Galaxy S20",
  "anio_fabricacion":"2023",
  "precio":"5000000",
  "marca":1, // ID de la marca
  "tipo":1, // ID del tipo
  "accesorio":1 // ID del accesorio
    }
```
Respuesta: 
```json
{
   "200 OK": "Teléfono creado exitosamente."
}
```

Endpoint: /telefono/ID del telefono a eliminar/eliminar
Respuesta:
```json
{
  "200 OK": "Teléfono eliminado con éxito."
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "No está autorizado para eliminar teléfonos."
}
```

##### MÉTODO GET: 


Endpoint: /telefono

Respuesta: 
```json
{
  "201 OK": {
    "accesorios": [
      [
        1,
        "Cargador Samsung"
      ],
      [
        3,
        "Funda Apple original"
      ],
      [
        4,
        "Cargador Apple"
      ]
    ],
    "marcas": [
      [
        1,
        "Samsumg"
      ],
      [
        2,
        "Apple"
      ],
      [
        3,
        "Motorola"
      ],
      [
        4,
        "Nokia"
      ],
      [
        5,
        "BlackBerry"
      ],
      [
        6,
        "Xiaomi"
      ],
      [
        7,
        "TCL"
      ],
      [
        8,
        "LG"
      ],
      [
        9,
        "Sony"
      ],
      [
        10,
        "ZTE"
      ],
      [
        11,
        "Oppo"
      ],
      [
        12,
        "Otra"
      ]
    ],
    "telefonos": [
      {
        "anio_fabricacion": 2023,
        "id": 1,
        "marca": {
          "id": 1,
          "nombre": "Samsumg"
        },
        "modelo": "Galaxy S20",
        "precio": 5000000,
        "tipo": {
          "id": 1,
          "nombre": "Gama alta"
        }
      }
    ],
    "tipos": [
      [
        1,
        "Gama alta"
      ],
      [
        3,
        "Gama baja"
      ]
    ]
  }
}
```


##### MÉTODO DELETE: 
Endpoint: /telefono/ID del telefono a eliminar

Respuesta: 
```json
{
  "200 OK": "Teléfono eliminado con éxito."
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "No está autorizado para eliminar teléfonos."
}
```

#### MAIN: 


##### MÉTODO GET: 
Endpoint: /main

Respuesta: 
```json
{
  "200 OK": {
    "telefonos": [
      {
        "id": 1,
        "modelo": "Galaxy S22",
        "anio_fabricacion": 2023,
        "precio": 5000000,
        "marca": "Samsung",
        "tipo": "Gama alta",
        "stock": [
          {
            "cantidad": 10
          },
          ...
        ]
      },
      ...
    ],
    "accesorios": [
      {
        "id": 1,
        "nombre": "Cargador Samsung"
      },
      ...
    ],
    "marcas": [
      {
        "id": 1,
        "nombre": "Samsung"
      },
      ...
    ],
    "tipos": [
      {
        "id": 1,
        "nombre": "Gama alta"
      },
      ...
    ],
    "total_stock_telefonos": 50
  }
}
```