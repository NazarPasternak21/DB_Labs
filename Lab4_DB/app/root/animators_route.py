from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import animator_controller
from ..domain.animators import Animator

animator_bp = Blueprint('animator', __name__, url_prefix='/animator')

@animator_bp.route('', methods=['GET'])
def get_all_animators() -> Response:
    animators = animator_controller.find_all_animators()
    animator_dtos = [animator.to_dict() for animator in animators if isinstance(animator, Animator)]
    return make_response(jsonify(animator_dtos), HTTPStatus.OK)

@animator_bp.route('', methods=['POST'])
def create_animator() -> Response:
    content = request.get_json()
    animator = Animator.from_dict(content)
    animator_controller.create_animator(animator)
    return make_response(jsonify(animator.to_dict()), HTTPStatus.CREATED)

@animator_bp.route('/<int:animator_id>', methods=['GET'])
def get_animator(animator_id: int) -> Response:
    return make_response(jsonify(animator_controller.find_animator_by_id(animator_id)), HTTPStatus.OK)

@animator_bp.route('/<int:animator_id>', methods=['PUT'])
def update_animator(animator_id: int) -> Response:
    content = request.get_json()
    animator = Animator.from_dict(content)
    animator_controller.update_animator(animator_id, animator)
    return make_response("Animator updated", HTTPStatus.OK)

@animator_bp.route('/<int:animator_id>', methods=['DELETE'])
def delete_animator(animator_id: int) -> Response:
    animator_controller.delete_animator(animator_id)
    return make_response("Animator deleted", HTTPStatus.OK)
