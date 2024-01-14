from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import cities_controller
from my_project.auth.domain import Cities

cities_bp = Blueprint('cities', __name__, url_prefix='/cities')

@cities_bp.get('')
def get_all_cities() -> Response:
    return make_response(jsonify(cities_controller.find_all()), HTTPStatus.OK)

@cities_bp.post('')
def create_city() -> Response:
    content = request.get_json()
    city = Cities.create_from_dto(content)
    cities_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.CREATED)

@cities_bp.get('/<int:city_id>')
def get_city(city_id: int) -> Response:
    return make_response(jsonify(cities_controller.find_by_id(city_id)), HTTPStatus.OK)

@cities_bp.put('/<int:city_id>')
def update_city(city_id: int) -> Response:
    content = request.get_json()
    city = Cities.create_from_dto(content)
    cities_controller.update(city_id, city)
    return make_response("City updated", HTTPStatus.OK)

@cities_bp.patch('/<int:city_id>')
def patch_city(city_id: int) -> Response:
    content = request.get_json()
    cities_controller.patch(city_id, content)
    return make_response("City updated", HTTPStatus.OK)

@cities_bp.delete('/<int:city_id>')
def delete_city(city_id: int) -> Response:
    cities_controller.delete(city_id)
    return make_response("City deleted", HTTPStatus.OK)
