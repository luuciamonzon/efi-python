from app import db
from flask import (
    Blueprint, 
    jsonify,
    request,
)


from flask_jwt_extended import (
    jwt_required,
    get_jwt,
)


from services.telefono_service import TelefonoService
from services.telefono_service import delete_with_accesorios
from repositories.telefono_repositories import TelefonoRepositories
from schemas import (
    AccesorioSchema,
    MarcaSchema, 
    TelefonoSchema, 
    TipoSchema, 
)


from models import Accesorio, Marca, Tipo
from forms import TelefonoForm


telefono_app_bp = Blueprint('telefono_app_bp', __name__)


@telefono_app_bp.route("/telefono", methods=['POST', 'GET'])
@jwt_required()
def telefonos():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear teléfonos"}), 403

    telefono_service = TelefonoService(TelefonoRepositories())
    telefonos = telefono_service.get_all()

    telefono_schema = TelefonoSchema(many=True)
    telefonos_serializados = telefono_schema.dump(telefonos)

    marcas = Marca.query.all()
    tipos = Tipo.query.all()
    accesorios = Accesorio.query.all()

    formulario = TelefonoForm()

    try:
        formulario.marca.choices = [(marca.id, marca.nombre) for marca in marcas]
        formulario.tipo.choices = [(tipo.id, tipo.nombre) for tipo in tipos]
        formulario.accesorio.choices = [(accesorio.id, accesorio.nombre) for accesorio in accesorios]
    except Exception as e:
        return jsonify({"error": f"Error al cargar las opciones del formulario: {str(e)}"}), 500

    if request.method == 'POST' and formulario.validate_on_submit():
        try:
            modelo = formulario.modelo.data
            anio_fabricacion = formulario.anio_fabricacion.data
            precio = formulario.precio.data
            marca = formulario.marca.data
            tipo = formulario.tipo.data

            telefono_service.create(modelo, anio_fabricacion, precio, marca, tipo)
            return jsonify({"message": "Teléfono creado exitosamente"}), 201
        except Exception as e:
            return jsonify({"error": f"Error al crear el teléfono: {str(e)}"}), 500

    return jsonify({
        "telefonos": telefonos_serializados,
        "marcas": [(marca.id, marca.nombre) for marca in marcas],
        "tipos": [(tipo.id, tipo.nombre) for tipo in tipos],
        "accesorios": [(accesorio.id, accesorio.nombre) for accesorio in accesorios]
    })


@telefono_app_bp.route("/telefono/<id>/eliminar", methods=['POST'])
@jwt_required()
def telefono_eliminar(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')
    
    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para eliminar teléfonos"}), 403

    telefono_service = TelefonoService(TelefonoRepositories())
    telefono_service.delete_with_accesorios(id)
    return jsonify({"message": "Teléfono eliminado con éxito"}), 200


@telefono_app_bp.route("/telefono/<id>", methods=['GET'])
@jwt_required()
def telefono_accesorio(id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para ver accesorios"}), 403

    telefono_service = TelefonoService(TelefonoRepositories())
    accesorios = telefono_service.get_accesorios_by_telefono(id)
    telefono = telefono_service.get_by_id(id)

    return jsonify({
        "telefono": telefono,
        "accesorios": accesorios
    })


@telefono_app_bp.route('/telefono/<int:telefono_id>', methods=['DELETE'])
@jwt_required()
def delete_telefono(telefono_id):
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para eliminar teléfonos"}), 403

    try:
        delete_with_accesorios(telefono_id)
        return jsonify({"message": "Teléfono eliminado con éxito"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    