# animators_dao.py
from .general_dao import GeneralDAO
from ..domain import Animator

class AnimatorDAO(GeneralDAO):
    _domain_type = Animator

    def find_all_animators(self):
        animators = self.find_all()
        print(f"Found animators: {animators}")
        return animators

    def find_animator_by_id(self, animator_id):
        return self.find_by_id(animator_id)

    def create_animator(self, animator):
        return self.create(animator)

    def create_all_animators(self, animator_list):
        return self.create_all(animator_list)

    def update_animator(self, animator_id, updated_animator):
        return self.update(animator_id, updated_animator)

    def patch_animator(self, animator_id, field_name, value):
        return self.patch(animator_id, field_name, value)

    def delete_animator(self, animator_id):
        return self.delete(animator_id)

    def delete_all_animators(self):
        return self.delete_all()
