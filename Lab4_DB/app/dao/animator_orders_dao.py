# animator_order_dao.py
from .general_dao import GeneralDAO
from ..domain import AnimatorOrder

class AnimatorOrderDAO(GeneralDAO):
    _domain_type = AnimatorOrder

    def find_all_animator_orders(self):
        animator_orders = self.find_all()
        print(f"Found animator orders: {animator_orders}")
        return animator_orders

    def find_animator_order_by_id(self, animator_order_id):
        return self.find_by_id(animator_order_id)

    def create_animator_order(self, animator_order):
        return self.create(animator_order)

    def create_all_animator_orders(self, animator_order_list):
        return self.create_all(animator_order_list)

    def update_animator_order(self, animator_order_id, updated_animator_order):
        return self.update(animator_order_id, updated_animator_order)

    def patch_animator_order(self, animator_order_id, field_name, value):
        return self.patch(animator_order_id, field_name, value)

    def delete_animator_order(self, animator_order_id):
        return self.delete(animator_order_id)

    def delete_all_animator_orders(self):
        return self.delete_all()
