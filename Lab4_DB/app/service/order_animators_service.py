# order_animators_service.py
from .general_service import GeneralService
from ..dao import order_animators_dao

class OrderAnimatorService(GeneralService):
    _dao = order_animators_dao

    def find_all(self):
        return self._dao.find_all_order_animators()

    def find_all_order_animators(self):
        return self._dao.find_all_order_animators()

    def find_order_animator_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_order_animator(self, order_animator):
        return self._dao.create(order_animator)

    def create_all_order_animators(self, order_animator_list):
        return self._dao.create_all(order_animator_list)

    def update_order_animator(self, key, new_order_animator):
        return self._dao.update(key, new_order_animator)

    def patch_order_animator(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_order_animator(self, key):
        return self._dao.delete(key)

    def delete_all_order_animators(self):
        return self._dao.delete_all()
