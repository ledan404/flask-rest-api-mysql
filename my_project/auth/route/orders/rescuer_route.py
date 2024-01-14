from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import rescuer_controller
from my_project.auth.domain.orders.rescuers import Rescuers

rescuers_bp = Blueprint('rescuers', __name__, url_prefix='/rescuers')

@rescuers_bp.get('')
def get_all_rescuers() -> Response:
    return make_response(jsonify(rescuer_controller.find_all()), HTTPStatus.OK)

@rescuers_bp.post('')
def create_rescuer() -> Response:
    content = request.get_json()
    rescuer = Rescuers.create_from_dto(content)
    rescuer_controller.create(rescuer)
    return make_response(jsonify(rescuer.put_into_dto()), HTTPStatus.CREATED)

@rescuers_bp.get('/<int:rescuer_id>')
def get_rescuer(rescuer_id: int) -> Response:
    return make_response(jsonify(rescuer_controller.find_by_id(rescuer_id)), HTTPStatus.OK)

@rescuers_bp.put('/<int:rescuer_id>')
def update_rescuer(rescuer_id: int) -> Response:
    content = request.get_json()
    rescuer = Rescuers.create_from_dto(content)
    rescuer_controller.update(rescuer_id, rescuer)
    return make_response("Rescuer updated", HTTPStatus.OK)

@rescuers_bp.patch('/<int:rescuer_id>')
def patch_rescuer(rescuer_id: int) -> Response:
    content = request.get_json()
    rescuer_controller.patch(rescuer_id, content)
    return make_response("Rescuer updated", HTTPStatus.OK)

@rescuers_bp.delete('/<int:rescuer_id>')
def delete_rescuer(rescuer_id: int) -> Response:
    rescuer_controller.delete(rescuer_id)
    return make_response("Rescuer deleted", HTTPStatus.OK)
