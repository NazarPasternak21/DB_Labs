# order_controller.py
from .general_controller import GeneralController
from ..service import orders_service

class OrderController(GeneralController):
    _service = orders_service.OrderService()

    def find_all_orders(self):
        return self.find_all()

    def find_order_by_id(self, key):
        return self.find_by_id(key)

    def create_order(self, order):
        return self.create(order)

    def create_all_orders(self, order_list):
        return self.create_all(order_list)

    def update_order(self, key, new_order):
        return self.update(key, new_order)

    def patch_order(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_order(self, key):
        return self.delete(key)

    def delete_all_orders(self):
        return self.delete_all()
