# event_type_service.py
from .general_service import GeneralService
from ..dao import event_types_dao

class EventTypeService(GeneralService):
    _dao = event_types_dao

    def find_all(self):
        return self._dao.find_all_event_types()
    def find_all_event_types(self):
        return self._dao.find_all_event_types()

    def find_event_type_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_event_type(self, event_type):
        return self._dao.create(event_type)

    def create_all_event_types(self, event_type_list):
        return self._dao.create_all(event_type_list)

    def update_event_type(self, key, new_event_type):
        return self._dao.update(key, new_event_type)

    def patch_event_type(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_event_type(self, key):
        return self._dao.delete(key)

    def delete_all_event_types(self):
        return self._dao.delete_all()
