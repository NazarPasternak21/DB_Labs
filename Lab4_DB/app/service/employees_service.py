# employee_service.py
from .general_service import GeneralService
from ..dao import employees_dao

class EmployeeService(GeneralService):
    _dao = employees_dao

    def find_all(self):
        return self._dao.find_all_employees()

    def find_all_employees(self):
        return self._dao.find_all_employees()

    def find_employee_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_employee(self, employee):
        return self._dao.create(employee)

    def create_all_employees(self, employee_list):
        return self._dao.create_all(employee_list)

    def update_employee(self, key, new_employee):
        return self._dao.update(key, new_employee)

    def patch_employee(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_employee(self, key):
        return self._dao.delete(key)

    def delete_all_employees(self):
        return self._dao.delete_all()
