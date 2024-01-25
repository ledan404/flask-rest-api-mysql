from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
from my_project.auth.controller import callers_controller
from my_project.auth.domain import Callers

callers_bp = Blueprint('callers', __name__, url_prefix='/callers')

@callers_bp.get('')
def get_all_callers() -> Response:
    return make_response(jsonify(callers_controller.find_all()), HTTPStatus.OK)

@callers_bp.get('/max_id')
def get_max_caller_id() -> Response:
    return make_response(jsonify(callers_controller.make_operation()), HTTPStatus.OK)

@callers_bp.post('')
def create_caller() -> Response:
    content = request.get_json()
    caller = Callers.create_from_dto(content)
    callers_controller.create(caller)
    return make_response(jsonify(caller.put_into_dto()), HTTPStatus.CREATED)

@callers_bp.get('/<int:caller_id>')
def get_caller(caller_id: int) -> Response:
    return make_response(jsonify(callers_controller.find_by_id(caller_id)), HTTPStatus.OK)

@callers_bp.put('/<int:caller_id>')
def update_caller(caller_id: int) -> Response:
    content = request.get_json()
    caller = Callers.create_from_dto(content)
    callers_controller.update(caller_id, caller)
    return make_response("Caller updated", HTTPStatus.OK)

@callers_bp.patch('/<int:caller_id>')
def patch_caller(caller_id: int) -> Response:
    content = request.get_json()
    callers_controller.patch(caller_id, content)
    return make_response("Caller updated", HTTPStatus.OK)

@callers_bp.delete('/<int:caller_id>')
def delete_caller(caller_id: int) -> Response:
    callers_controller.delete(caller_id)
    return make_response("Caller deleted", HTTPStatus.OK)
