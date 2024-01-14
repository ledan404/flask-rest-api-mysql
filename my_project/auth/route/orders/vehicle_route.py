from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import vehicles_controller
from my_project.auth.domain import Vehicles

vehicles_bp = Blueprint('vehicles', __name__, url_prefix='/vehicles')

@vehicles_bp.get('')
def get_all_vehicles() -> Response:
    return make_response(jsonify(vehicles_controller.find_all()), HTTPStatus.OK)

@vehicles_bp.post('')
def create_vehicle() -> Response:
    content = request.get_json()
    vehicle = Vehicles.create_from_dto(content)
    vehicles_controller.create(vehicle)
    return make_response(jsonify(vehicle.put_into_dto()), HTTPStatus.CREATED)

@vehicles_bp.get('/<int:vehicle_id>')
def get_vehicle(vehicle_id: int) -> Response:
    return make_response(jsonify(vehicles_controller.find_by_id(vehicle_id)), HTTPStatus.OK)

@vehicles_bp.put('/<int:vehicle_id>')
def update_vehicle(vehicle_id: int) -> Response:
    content = request.get_json()
    vehicle = Vehicles.create_from_dto(content)
    vehicles_controller.update(vehicle_id, vehicle)
    return make_response("Vehicle updated", HTTPStatus.OK)

@vehicles_bp.patch('/<int:vehicle_id>')
def patch_vehicle(vehicle_id: int) -> Response:
    content = request.get_json()
    vehicles_controller.patch(vehicle_id, content)
    return make_response("Vehicle updated", HTTPStatus.OK)

@vehicles_bp.delete('/<int:vehicle_id>')
def delete_vehicle(vehicle_id: int) -> Response:
    vehicles_controller.delete(vehicle_id)
    return make_response("Vehicle deleted", HTTPStatus.OK)
