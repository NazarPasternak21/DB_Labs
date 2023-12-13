from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import employee_controller
from ..domain.employees import Employee

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

@employee_bp.route('', methods=['GET'])
def get_all_employees() -> Response:
    employees = employee_controller.find_all_employees()
    employee_dtos = [employee.to_dict() for employee in employees if isinstance(employee, Employee)]
    return make_response(jsonify(employee_dtos), HTTPStatus.OK)

@employee_bp.route('', methods=['POST'])
def create_employee() -> Response:
    content = request.get_json()
    employee = Employee.from_dict(content)
    employee_controller.create_employee(employee)
    return make_response(jsonify(employee.to_dict()), HTTPStatus.CREATED)

@employee_bp.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id: int) -> Response:
    return make_response(jsonify(employee_controller.find_employee_by_id(employee_id)), HTTPStatus.OK)

@employee_bp.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id: int) -> Response:
    content = request.get_json()
    employee = Employee.from_dict(content)
    employee_controller.update_employee(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)

@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id: int) -> Response:
    employee_controller.delete_employee(employee_id)
    return make_response("Employee deleted", HTTPStatus.OK)
