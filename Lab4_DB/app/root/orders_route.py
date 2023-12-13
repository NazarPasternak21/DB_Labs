from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import order_controller
from ..domain.orders import Order

order_bp = Blueprint('order', __name__, url_prefix='/order')

@order_bp.route('', methods=['GET'])
def get_all_orders() -> Response:
    orders = order_controller.find_all_orders()
    order_dtos = [order.to_dict() for order in orders if isinstance(order, Order)]
    return make_response(jsonify(order_dtos), HTTPStatus.OK)

@order_bp.route('', methods=['POST'])
def create_order() -> Response:
    content = request.get_json()
    order = Order.from_dict(content)
    order_controller.create_order(order)
    return make_response(jsonify(order.to_dict()), HTTPStatus.CREATED)

@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id: int) -> Response:
    return make_response(jsonify(order_controller.find_order_by_id(order_id)), HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id: int) -> Response:
    content = request.get_json()
    order = Order.from_dict(content)
    order_controller.update_order(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id: int) -> Response:
    order_controller.delete_order(order_id)
    return make_response("Order deleted", HTTPStatus.OK)
