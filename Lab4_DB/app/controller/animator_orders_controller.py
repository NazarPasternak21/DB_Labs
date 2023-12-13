# animator_order_controller.py
from .general_controller import GeneralController
from ..service import animator_orders_service

class AnimatorOrderController(GeneralController):
    _service = animator_orders_service.AnimatorOrderService()

    def find_all_animator_orders(self):
        return self.find_all()

    def find_animator_order_by_id(self, key):
        return self.find_by_id(key)

    def create_animator_order(self, animator_order):
        return self.create(animator_order)

    def create_all_animator_orders(self, animator_order_list):
        return self.create_all(animator_order_list)

    def update_animator_order(self, key, new_animator_order):
        return self.update(key, new_animator_order)

    def patch_animator_order(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_animator_order(self, key):
        return self.delete(key)

    def delete_all_animator_orders(self):
        return self.delete_all()
