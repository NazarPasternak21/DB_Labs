from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import event_type_controller
from ..domain.event_types import EventType

event_type_bp = Blueprint('event_type', __name__, url_prefix='/event_type')

@event_type_bp.route('', methods=['GET'])
def get_all_event_types() -> Response:
    event_types = event_type_controller.find_all_event_types()
    event_type_dtos = [event_type.to_dict() for event_type in event_types if isinstance(event_type, EventType)]
    return make_response(jsonify(event_type_dtos), HTTPStatus.OK)

@event_type_bp.route('', methods=['POST'])
def create_event_type() -> Response:
    content = request.get_json()
    event_type = EventType.from_dict(content)
    event_type_controller.create_event_type(event_type)
    return make_response(jsonify(event_type.to_dict()), HTTPStatus.CREATED)

@event_type_bp.route('/<int:event_type_id>', methods=['GET'])
def get_event_type(event_type_id: int) -> Response:
    return make_response(jsonify(event_type_controller.find_event_type_by_id(event_type_id)), HTTPStatus.OK)

@event_type_bp.route('/<int:event_type_id>', methods=['PUT'])
def update_event_type(event_type_id: int) -> Response:
    content = request.get_json()
    event_type = EventType.from_dict(content)
    event_type_controller.update_event_type(event_type_id, event_type)
    return make_response("Event Type updated", HTTPStatus.OK)

@event_type_bp.route('/<int:event_type_id>', methods=['DELETE'])
def delete_event_type(event_type_id: int) -> Response:
    event_type_controller.delete_event_type(event_type_id)
    return make_response("Event Type deleted", HTTPStatus.OK)
