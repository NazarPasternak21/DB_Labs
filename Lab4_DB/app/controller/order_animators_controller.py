# order_animator_controller.py
from .general_controller import GeneralController
from ..service import order_animators_service

class OrderAnimatorController(GeneralController):
    _service = order_animators_service.OrderAnimatorService()

    def find_all_order_animators(self):
        return self.find_all()

    def find_order_animator_by_id(self, key):
        return self.find_by_id(key)

    def create_order_animator(self, order_animator):
        return self.create(order_animator)

    def create_all_order_animators(self, order_animator_list):
        return self.create_all(order_animator_list)

    def update_order_animator(self, key, new_order_animator):
        return self.update(key, new_order_animator)

    def patch_order_animator(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_order_animator(self, key):
        return self.delete(key)

    def delete_all_order_animators(self):
        return self.delete_all()
