# order_service.py
from .general_service import GeneralService
from ..dao import orders_dao

class OrderService(GeneralService):
    _dao = orders_dao

    def find_all(self):
        return self._dao.find_all_orders()

    def find_all_orders(self):
        return self._dao.find_all_orders()

    def find_order_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_order(self, order):
        return self._dao.create(order)

    def create_all_orders(self, order_list):
        return self._dao.create_all(order_list)

    def update_order(self, key, new_order):
        return self._dao.update(key, new_order)

    def patch_order(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_order(self, key):
        return self._dao.delete(key)

    def delete_all_orders(self):
        return self._dao.delete_all()
