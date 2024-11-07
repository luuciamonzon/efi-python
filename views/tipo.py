from app import db
from flask import Blueprint, request, jsonify


from flask_jwt_extended import (
    jwt_required,
    get_jwt,
)


from services.tipo_service import TipoService
from repositories.tipo_repositories import TipoRepositories
from schemas import TipoSchema
from forms import TipoForm


tipo_app_bp = Blueprint('tipo_app_bp', __name__)


@tipo_app_bp.route("/tipo", methods=['GET', 'POST'])
@jwt_required()
def tipos():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para crear tipos"}), 403

    tipo_service = TipoService(TipoRepositories())
    tipos = tipo_service.get_all()

    tipo_schema = TipoSchema(many=True)
    tipos_serializados = tipo_schema.dump(tipos)

    formulario = TipoForm()
    if request.method == 'POST' and formulario.validate_on_submit():
        nombre = formulario.nombre.data
        tipo_service.create(nombre)
        return jsonify({'Mensaje': 'Tipo creado exitosamente'}), 201

    return jsonify({'tipos': tipos_serializados})


@tipo_app_bp.route('/tipo/<int:id>/eliminar', methods=['POST'])
@jwt_required()
def tipo_eliminar(id):
    additional_info = get_jwt()
    administrador = additional_info.get('administrador')

    if not administrador:
        return jsonify({"Mensaje": "No está autorizado para eliminar tipos"}), 403

    tipo_service = TipoService(TipoRepositories())
    tipo = tipo_service.get_by_id(id)
    if tipo:
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'Mensaje': 'Tipo eliminado exitosamente'}), 200
    return jsonify({'error': 'Tipo no encontrado'}), 404
