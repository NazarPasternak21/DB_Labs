# animator_service.py
from .general_service import GeneralService
from ..dao import animators_dao

class AnimatorService(GeneralService):
    _dao = animators_dao

    def find_all(self):
        return self._dao.find_all_animators()

    def find_all_animators(self):
        return self._dao.find_all_animators()

    def find_animator_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_animator(self, animator):
        return self._dao.create(animator)

    def create_all_animators(self, animator_list):
        return self._dao.create_all(animator_list)

    def update_animator(self, key, new_animator):
        return self._dao.update(key, new_animator)

    def patch_animator(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_animator(self, key):
        return self._dao.delete(key)

    def delete_all_animators(self):
        return self._dao.delete_all()
