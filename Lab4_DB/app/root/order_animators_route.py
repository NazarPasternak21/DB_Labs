from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import order_animator_controller
from ..domain.order_animators import OrderAnimator

order_animator_bp = Blueprint('order_animator', __name__, url_prefix='/order_animator')

@order_animator_bp.route('', methods=['GET'])
def get_all_order_animators() -> Response:
    order_animators = order_animator_controller.find_all_order_animators()
    order_animator_dtos = [order_animator.to_dict() for order_animator in order_animators if isinstance(order_animator, OrderAnimator)]
    return make_response(jsonify(order_animator_dtos), HTTPStatus.OK)

@order_animator_bp.route('', methods=['POST'])
def create_order_animator() -> Response:
    content = request.get_json()
    order_animator = OrderAnimator.from_dict(content)
    order_animator_controller.create_order_animator(order_animator)
    return make_response(jsonify(order_animator.to_dict()), HTTPStatus.CREATED)

@order_animator_bp.route('/<int:order_animator_id>', methods=['GET'])
def get_order_animator(order_animator_id: int) -> Response:
    return make_response(jsonify(order_animator_controller.find_order_animator_by_id(order_animator_id)), HTTPStatus.OK)

@order_animator_bp.route('/<int:order_animator_id>', methods=['PUT'])
def update_order_animator(order_animator_id: int) -> Response:
    content = request.get_json()
    order_animator = OrderAnimator.from_dict(content)
    order_animator_controller.update_order_animator(order_animator_id, order_animator)
    return make_response("Order Animator updated", HTTPStatus.OK)

@order_animator_bp.route('/<int:order_animator_id>', methods=['DELETE'])
def delete_order_animator(order_animator_id: int) -> Response:
    order_animator_controller.delete_order_animator(order_animator_id)
    return make_response("Order Animator deleted", HTTPStatus.OK)
