# employee_controller.py
from .general_controller import GeneralController
from ..service import employees_service

class EmployeeController(GeneralController):
    _service = employees_service.EmployeeService()

    def find_all_employees(self):
        return self.find_all()

    def find_employee_by_id(self, key):
        return self.find_by_id(key)

    def create_employee(self, employee):
        return self.create(employee)

    def create_all_employees(self, employee_list):
        return self.create_all(employee_list)

    def update_employee(self, key, new_employee):
        return self.update(key, new_employee)

    def patch_employee(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_employee(self, key):
        return self.delete(key)

    def delete_all_employees(self):
        return self.delete_all()
