from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import client_controller
from ..domain.clients import Client

client_bp = Blueprint('client', __name__, url_prefix='/client')

@client_bp.route('', methods=['GET'])
def get_all_clients() -> Response:
    clients = client_controller.find_all_clients()
    client_dtos = [client.to_dict() for client in clients if isinstance(client, Client)]
    return make_response(jsonify(client_dtos), HTTPStatus.OK)

@client_bp.route('', methods=['POST'])
def create_client() -> Response:
    content = request.get_json()
    client = Client.from_dict(content)
    client_controller.create_client(client)
    return make_response(jsonify(client.to_dict()), HTTPStatus.CREATED)

@client_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id: int) -> Response:
    return make_response(jsonify(client_controller.find_client_by_id(client_id)), HTTPStatus.OK)

@client_bp.route('/<int:client_id>', methods=['PUT'])
def update_client(client_id: int) -> Response:
    content = request.get_json()
    client = Client.from_dict(content)
    client_controller.update_client(client_id, client)
    return make_response("Client updated", HTTPStatus.OK)

@client_bp.route('/<int:client_id>', methods=['DELETE'])
def delete_client(client_id: int) -> Response:
    client_controller.delete_client(client_id)
    return make_response("Client deleted", HTTPStatus.OK)
