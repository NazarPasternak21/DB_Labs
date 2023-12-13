# animator_order_service.py
from .general_service import GeneralService
from ..dao import animator_orders_dao

class AnimatorOrderService(GeneralService):
    _dao = animator_orders_dao

    def find_all(self):
        return self._dao.find_all_animator_orders()

    def find_all_animator_orders(self):
        return self._dao.find_all_animator_orders()

    def find_animator_order_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_animator_order(self, animator_order):
        return self._dao.create(animator_order)

    def create_all_animator_orders(self, animator_order_list):
        return self._dao.create_all(animator_order_list)

    def update_animator_order(self, key, new_animator_order):
        return self._dao.update(key, new_animator_order)

    def patch_animator_order(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_animator_order(self, key):
        return self._dao.delete(key)

    def delete_all_animator_orders(self):
        return self._dao.delete_all()
