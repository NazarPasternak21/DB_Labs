from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import animator_order_controller
from ..domain.animator_orders import AnimatorOrder

animator_order_bp = Blueprint('animator_order', __name__, url_prefix='/animator_order')

@animator_order_bp.route('', methods=['GET'])
def get_all_animator_orders() -> Response:
    animator_orders = animator_order_controller.find_all_animator_orders()
    animator_order_dtos = [animator_order.to_dict() for animator_order in animator_orders if isinstance(animator_order, AnimatorOrder)]
    return make_response(jsonify(animator_order_dtos), HTTPStatus.OK)

@animator_order_bp.route('', methods=['POST'])
def create_animator_order() -> Response:
    content = request.get_json()
    animator_order = AnimatorOrder.from_dict(content)
    animator_order_controller.create_animator_order(animator_order)
    return make_response(jsonify(animator_order.to_dict()), HTTPStatus.CREATED)

@animator_order_bp.route('/<int:animator_order_id>', methods=['GET'])
def get_animator_order(animator_order_id: int) -> Response:
    return make_response(jsonify(animator_order_controller.find_animator_order_by_id(animator_order_id)), HTTPStatus.OK)

@animator_order_bp.route('/<int:animator_order_id>', methods=['PUT'])
def update_animator_order(animator_order_id: int) -> Response:
    content = request.get_json()
    animator_order = AnimatorOrder.from_dict(content)
    animator_order_controller.update_animator_order(animator_order_id, animator_order)
    return make_response("Animator Order updated", HTTPStatus.OK)

@animator_order_bp.route('/<int:animator_order_id>', methods=['DELETE'])
def delete_animator_order(animator_order_id: int) -> Response:
    animator_order_controller.delete_animator_order(animator_order_id)
    return make_response("Animator Order deleted", HTTPStatus.OK)
