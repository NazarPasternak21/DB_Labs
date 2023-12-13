# order_animator_dao.py
from .general_dao import GeneralDAO
from ..domain import OrderAnimator

class OrderAnimatorDAO(GeneralDAO):
    _domain_type = OrderAnimator

    def find_all_order_animators(self):
        order_animators = self.find_all()
        print(f"Found order animators: {order_animators}")
        return order_animators

    def find_order_animator_by_id(self, order_animator_id):
        return self.find_by_id(order_animator_id)

    def create_order_animator(self, order_animator):
        return self.create(order_animator)

    def create_all_order_animators(self, order_animator_list):
        return self.create_all(order_animator_list)

    def update_order_animator(self, order_animator_id, updated_order_animator):
        return self.update(order_animator_id, updated_order_animator)

    def patch_order_animator(self, order_animator_id, field_name, value):
        return self.patch(order_animator_id, field_name, value)

    def delete_order_animator(self, order_animator_id):
        return self.delete(order_animator_id)

    def delete_all_order_animators(self):
        return self.delete_all()
