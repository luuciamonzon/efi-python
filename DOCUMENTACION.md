## DOCUMENTACIÓN DE ENDPOINTS: 


# NOTA GENERAL:
Todos los endpoints requieren que el usuario esté autenticado y tenga permisos de administrador para realizar acciones específicas. En caso de errores, se proporcionan mensajes claros que indican el problema.

## LOGIN : 


# METODO POST / AUTENTICACIÓN
Endpoint : /login
Cuerpo de la solicitud: 
`
    {
    "username":"admin",
    "password" "123"
    }
`
Respuesta: 
`
    {
    "toker":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."
    }
`


## USERS: 


## METODO POST 

Endpoint : /users
Cuerpo de la solicitud: 
`
    {
    "username":"luucia",
    "password" "monzon1"
    }
`
Respuesta: 
`
{
  "Mensaje": "Usuario creado correctamente",
  "Usuario": {
  "username": "nuevo_usuario",
  "is_admin": true
  }
}
`
Mensajes de error:
`
 {
    `403 Forbidden`: Solo los administradores pueden crear usuarios.
    `500 Internal Server Error`: Fallo la creación del usuario.
 }
`

## METODO GET

Si el usuario autenticado es administrador, se devuelve la lista completa con detalles de cada usuario. Si el usuario no es administrador, se devuelve una versión mínima de los datos del usuario.

## METODO DELETE

Endpoint : /users/ID del usuario a eliminar/delete
Respuesta:
`
{
  "Mensaje": "Usuario eliminado correctamente"
}
`
Mensajes en caso de errores: 
Si no es usuario admin: {"Mensaje": "Solo el admin puede eliminar usuarios"}), 403
Si no encuentra al usuario: {"Mensaje": "Usuario no encontrado"}), 404
Si no se pudo eliminar el usuario: {"Mensaje": "Fallo al eliminar el usuario", "Error": str(e)}), 500


## METODO PUT 

Endpoint : /users/ID del usuario a actualizar/update
Cuerpo de la solicitud: 
`
    {
    "username":"dato a actualizar, si se desea",
    "password" "dato a actualizar, si se desea"
    }
`
Respuesta:
`
{
  "Mensaje": "Usuario actualizado correctamente", "Usuario": user.to_dict()}), 200
}
`
Mensajes en caso de errores: 
Si no es usuario admin: {"Mensaje": "No tienes permiso para actualizar usuarios"}), 403
Si no encuentra al usuario: {"Mensaje": "Usuario no encontrado"}), 404
Si no se pudo actualizar el usuario: "Mensaje": "Error al actualizar el usuario: " + str(e)}), 500


## MARCA: 


## METODO POST


Endpoint : /marca
Cuerpo de la solicitud: 
`
    {
    "nombre":"Nombre de la marca a crear"
    }
`
Respuesta:
`
"marcas": 
    {
      "id": 1,
      "nombre": "Samsumg"
    }
`
Mensajes en caso de errores: 
Si no es usuario admin: {"Mensaje": "No está autorizado para crear marcas"}), 403, 
"Mensaje": "No está autorizado para editar marca"}), 403


## METODO GET 
Endpoint : /marca
Respuesta: 
`
{
  "marcas": [
    {
      "id": 1,
      "nombre": "Samsumg"
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
    },
    {
      "id": 6,
      "nombre": "Xiaomi"
    },
    {
      "id": 7,
      "nombre": "TCL"
    },
    {
      "id": 8,
      "nombre": "LG"
    },
    {
      "id": 9,
      "nombre": "Sony"
    }
  ]
}
`


## STOCK: 

## METODO POST: 
Endpoint : /stock

Endpoint : /eliminar_stock
Respuesta:
`
 return jsonify({"Mensaje": "Stock restado correctamente"}), 200
`
Mensajes en caso de error: 
Si no es usuario admin: "Mensaje": "No está autorizado para acceder a esta ruta"}), 403; "Mensaje": "No está autorizado para borrar stock"}), 403
Si faltan parámetros requeridos o si la cantidad no es un número entero: "Mensaje": "Debe proporcionar 'telefono_id' y 'cantidad'"}), 400; "Mensaje": "Cantidad debe ser un número entero"}), 400
Si no se utilizan los datos correctos: {"Mensaje": "Datos inválidos"}), 400


## METODO GET: 

Endpoint : /stock
Respuesta:
[
  {
    "telefono": "Modelo del teléfono",
    "stock": cantidad
  },
  ...
]

## ACCESORIOS: 

## METODO POST: 


## METODO GET: 



## TIPO: 


## METODO POST: 
Endpoint : /tipo
Cuerpo de la solicitud: 
`
    {
    "nombre":"tipo"
    }
`
Respuesta: 
`
{
  jsonify({'Mensaje': 'Tipo creado exitosamente'}), 201
}
`

Endpoint: /tipo/ID del tipo a eliminar/eliminar
Respuesta: 
`
{
  jsonify({'Mensaje': 'Tipo eliminado exitosamente'}), 200
}
`
Mensaje en caso de error: 
Si no es usuario admin: "Mensaje": "No está autorizado para crear tipos"}), 403
"Mensaje":"No está autorizado para eliminar tipos"}), 403
Si no encuentra el tipo solicitado: jsonify({'error': 'Tipo no encontrado'}), 404


## METODO GET: 
Endpoint : /tipo
Respuesta: Listado de tipos.

## TELEFONO: 


## METODO POST: 


## METODO GET: 


## MAIN: 

## METODO POST: 


## METODO GET: 