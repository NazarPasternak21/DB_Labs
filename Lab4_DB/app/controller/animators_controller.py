# animator_controller.py
from .general_controller import GeneralController
from ..service import animator_service

class AnimatorController(GeneralController):
    _service = animator_service

    def find_all_animators(self):
        return self.find_all()

    def find_animator_by_id(self, key):
        return self.find_by_id(key)

    def create_animator(self, animator):
        return self.create(animator)

    def create_all_animators(self, animator_list):
        return self.create_all(animator_list)

    def update_animator(self, key, new_animator):
        return self.update(key, new_animator)

    def patch_animator(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_animator(self, key):
        return self.delete(key)

    def delete_all_animators(self):
        return self.delete_all()
