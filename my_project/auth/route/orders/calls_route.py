from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
from my_project.auth.controller import calls_controller
from my_project.auth.domain.orders.calls import Calls

calls_bp = Blueprint('calls', __name__, url_prefix='/calls')

@calls_bp.get('')
def get_all_calls() -> Response:
    return make_response(jsonify(calls_controller.find_all()), HTTPStatus.OK)

@calls_bp.post('')
def create_call() -> Response:
    content = request.get_json()
    call = Calls.create_from_dto(content)
    calls_controller.create(call)
    return make_response(jsonify(call.put_into_dto()), HTTPStatus.CREATED)

@calls_bp.get('/<int:call_id>')
def get_call(call_id: int) -> Response:
    return make_response(jsonify(calls_controller.find_by_id(call_id)), HTTPStatus.OK)

@calls_bp.put('/<int:call_id>')
def update_call(call_id: int) -> Response:
    content = request.get_json()
    call = Calls.create_from_dto(content)
    calls_controller.update(call_id, call)
    return make_response("Call updated", HTTPStatus.OK)

@calls_bp.patch('/<int:call_id>')
def patch_call(call_id: int) -> Response:
    content = request.get_json()
    calls_controller.patch(call_id, content)
    return make_response("Call updated", HTTPStatus.OK)

@calls_bp.delete('/<int:call_id>')
def delete_call(call_id: int) -> Response:
    calls_controller.delete(call_id)
    return make_response("Call deleted", HTTPStatus.OK)
