# order_dao.py
from .general_dao import GeneralDAO
from ..domain import Order

class OrderDAO(GeneralDAO):
    _domain_type = Order

    def find_all_orders(self):
        orders = self.find_all()
        print(f"Found orders: {orders}")
        return orders

    def find_order_by_id(self, order_id):
        return self.find_by_id(order_id)

    def create_order(self, order):
        return self.create(order)

    def create_all_orders(self, order_list):
        return self.create_all(order_list)

    def update_order(self, order_id, updated_order):
        return self.update(order_id, updated_order)

    def patch_order(self, order_id, field_name, value):
        return self.patch(order_id, field_name, value)

    def delete_order(self, order_id):
        return self.delete(order_id)

    def delete_all_orders(self):
        return self.delete_all()
