# event_type_controller.py
from .general_controller import GeneralController
from ..service import event_types_service

class EventTypeController(GeneralController):
    _service = event_types_service.EventTypeService()
    def find_all_event_types(self):
        return self.find_all()

    def find_event_type_by_id(self, key):
        return self.find_by_id(key)

    def create_event_type(self, event_type):
        return self.create(event_type)

    def create_all_event_types(self, event_type_list):
        return self.create_all(event_type_list)

    def update_event_type(self, key, new_event_type):
        return self.update(key, new_event_type)

    def patch_event_type(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_event_type(self, key):
        return self.delete(key)

    def delete_all_event_types(self):
        return self.delete_all()
