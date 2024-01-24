from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import call_vehicle_controller
from my_project.auth.domain import CallVehicles

call_vehicles_bp = Blueprint('call_vehicles', __name__, url_prefix='/call_vehicles')

@call_vehicles_bp.get('')
def get_all_call_vehicles() -> Response:
    return make_response(jsonify(call_vehicle_controller.find_all()), HTTPStatus.OK)

@call_vehicles_bp.get('/call/<int:call_id>')
def get_call_vehicles(call_id: int) -> Response:
    return make_response(jsonify(call_vehicle_controller.find_vehicles_for_call(call_id)), HTTPStatus.OK)

@call_vehicles_bp.post('')
def create_call_vehicle() -> Response:
    content = request.get_json()
    call_vehicle = CallVehicles.create_from_dto(content)
    call_vehicle_controller.create(call_vehicle)
    return make_response(jsonify(call_vehicle.put_into_dto()), HTTPStatus.CREATED)

@call_vehicles_bp.get('/<int:call_vehicle_id>')
def get_call_vehicle(call_vehicle_id: int) -> Response:
    return make_response(jsonify(call_vehicle_controller.find_by_id(call_vehicle_id)), HTTPStatus.OK)

@call_vehicles_bp.put('/<int:call_vehicle_id>')
def update_call_vehicle(call_vehicle_id: int) -> Response:
    content = request.get_json()
    call_vehicle = CallVehicles.create_from_dto(content)
    call_vehicle_controller.update(call_vehicle_id, call_vehicle)
    return make_response("CallVehicle updated", HTTPStatus.OK)

@call_vehicles_bp.patch('/<int:call_vehicle_id>')
def patch_call_vehicle(call_vehicle_id: int) -> Response:
    content = request.get_json()
    call_vehicle_controller.patch(call_vehicle_id, content)
    return make_response("CallVehicle updated", HTTPStatus.OK)

@call_vehicles_bp.delete('/<int:call_vehicle_id>')
def delete_call_vehicle(call_vehicle_id: int) -> Response:
    call_vehicle_controller.delete(call_vehicle_id)
    return make_response("CallVehicle deleted", HTTPStatus.OK)
