from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
from my_project.auth.controller import rescuer_call_controller
from my_project.auth.domain.orders.rescuer_calls import RescuerCalls

rescuer_calls_bp = Blueprint('rescuer_calls', __name__, url_prefix='/rescuer-calls')

@rescuer_calls_bp.get('')
def get_all_rescuer_calls() -> Response:
    return make_response(jsonify(rescuer_call_controller.find_all()), HTTPStatus.OK)

@rescuer_calls_bp.get('/rescuer/<int:rescuer_id>')
def get_rescuer_calls(rescuer_id: int) -> Response:
    return make_response(jsonify(rescuer_call_controller.find_rescuers(rescuer_id)), HTTPStatus.OK)

@rescuer_calls_bp.post('')
def create_rescuer_call() -> Response:
    content = request.get_json()
    rescuer_call = RescuerCalls.create_from_dto(content)
    rescuer_call_controller.create(rescuer_call)
    return make_response(jsonify(rescuer_call.put_into_dto()), HTTPStatus.CREATED)

@rescuer_calls_bp.get('/<int:rescuer_call_id>')
def get_rescuer_call(rescuer_call_id: int) -> Response:
    return make_response(jsonify(rescuer_call_controller.find_by_id(rescuer_call_id)), HTTPStatus.OK)

@rescuer_calls_bp.put('/<int:rescuer_call_id>')
def update_rescuer_call(rescuer_call_id: int) -> Response:
    content = request.get_json()
    rescuer_call = RescuerCalls.create_from_dto(content)
    rescuer_call_controller.update(rescuer_call_id, rescuer_call)
    return make_response("Rescuer call updated", HTTPStatus.OK)

@rescuer_calls_bp.patch('/<int:rescuer_call_id>')
def patch_rescuer_call(rescuer_call_id: int) -> Response:
    content = request.get_json()
    rescuer_call_controller.patch(rescuer_call_id, content)
    return make_response("Rescuer call updated", HTTPStatus.OK)

@rescuer_calls_bp.delete('/<int:rescuer_call_id>')
def delete_rescuer_call(rescuer_call_id: int) -> Response:
    rescuer_call_controller.delete(rescuer_call_id)
    return make_response("Rescuer call deleted", HTTPStatus.OK)
