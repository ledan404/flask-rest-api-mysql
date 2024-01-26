from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus
from my_project.auth.controller import injuries_controller
from my_project.auth.domain.orders.injuries import Injuries

injuries_bp = Blueprint('injuries', __name__, url_prefix='/injuries')

@injuries_bp.get('')
def get_injuries() -> Response:
    return make_response(jsonify(injuries_controller.find_all()), HTTPStatus.OK)

@injuries_bp.get('/call/<int:call_id>')
def get_injuries_by_call(call_id: int) -> Response:
    return make_response(jsonify(injuries_controller.find_injuries(call_id)), HTTPStatus.OK)

@injuries_bp.get('/rescuer/<int:rescuer_id>')
def get_injuries_by_rescuer(rescuer_id: int) -> Response:
    return make_response(jsonify(injuries_controller.find_rescuer(rescuer_id)), HTTPStatus.OK)


@injuries_bp.post('')
def create_injury() -> Response:
    content = request.get_json()
    injury = Injuries.create_from_dto(content)
    injuries_controller.create(injury)
    return make_response(jsonify(injury.put_into_dto()), HTTPStatus.CREATED)

@injuries_bp.get('/<int:injury_id>')
def get_injury(injury_id: int) -> Response:
    return make_response(jsonify(injuries_controller.find_by_id(injury_id)), HTTPStatus.OK)

@injuries_bp.put('/<int:injury_id>')
def update_injury(injury_id: int) -> Response:
    content = request.get_json()
    injury = Injuries.create_from_dto(content)
    injuries_controller.update(injury_id, injury)
    return make_response("Injury updated", HTTPStatus.OK)

@injuries_bp.patch('/<int:injury_id>')
def patch_injury(injury_id: int) -> Response:
    content = request.get_json()
    injuries_controller.patch(injury_id, content)
    return make_response("Injury updated", HTTPStatus.OK)

@injuries_bp.delete('/<int:injury_id>')
def delete_injury(injury_id: int) -> Response:
    injuries_controller.delete(injury_id)
    return make_response("Injury deleted", HTTPStatus.OK)
