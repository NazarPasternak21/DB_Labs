# employee_dao.py
from .general_dao import GeneralDAO
from ..domain import Employee

class EmployeeDAO(GeneralDAO):
    _domain_type = Employee

    def find_all_employees(self):
        employees = self.find_all()
        print(f"Found employees: {employees}")
        return employees

    def find_employee_by_id(self, employee_id):
        return self.find_by_id(employee_id)

    def create_employee(self, employee):
        return self.create(employee)

    def create_all_employees(self, employee_list):
        return self.create_all(employee_list)

    def update_employee(self, employee_id, updated_employee):
        return self.update(employee_id, updated_employee)

    def patch_employee(self, employee_id, field_name, value):
        return self.patch(employee_id, field_name, value)

    def delete_employee(self, employee_id):
        return self.delete(employee_id)

    def delete_all_employees(self):
        return self.delete_all()
