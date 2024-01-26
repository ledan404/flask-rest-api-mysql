from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
from my_project.auth.controller import emergency_reasons_controller
from my_project.auth.domain import EmergencyReasons

emergency_reasons_bp = Blueprint('emergency_reasons', __name__, url_prefix='/emergency_reasons')

@emergency_reasons_bp.get('')
def get_all_emergency_reasons() -> Response:
    return make_response(jsonify(emergency_reasons_controller.find_all()), HTTPStatus.OK)

@emergency_reasons_bp.post('')
def create_emergency_reason() -> Response:
    content = request.get_json()
    emergency_reason = EmergencyReasons.create_from_dto(content)
    emergency_reasons_controller.create(emergency_reason)
    return make_response(jsonify(emergency_reason.put_into_dto()), HTTPStatus.CREATED)

@emergency_reasons_bp.get('/<int:emergency_reason_id>')
def get_emergency_reason(emergency_reason_id: int) -> Response:
    return make_response(jsonify(emergency_reasons_controller.find_by_id(emergency_reason_id)), HTTPStatus.OK)

@emergency_reasons_bp.put('/<int:emergency_reason_id>')
def update_emergency_reason(emergency_reason_id: int) -> Response:
    content = request.get_json()
    emergency_reason = EmergencyReasons.create_from_dto(content)
    emergency_reasons_controller.update(emergency_reason_id, emergency_reason)
    return make_response("Emergency reason updated", HTTPStatus.OK)

@emergency_reasons_bp.patch('/<int:emergency_reason_id>')
def patch_emergency_reason(emergency_reason_id: int) -> Response:
    content = request.get_json()
    emergency_reasons_controller.patch(emergency_reason_id, content)
    return make_response("Emergency reason updated", HTTPStatus.OK)

@emergency_reasons_bp.delete('/<int:emergency_reason_id>')
def delete_emergency_reason(emergency_reason_id: int) -> Response:
    emergency_reasons_controller.delete(emergency_reason_id)
    return make_response("Emergency reason deleted", HTTPStatus.OK)
