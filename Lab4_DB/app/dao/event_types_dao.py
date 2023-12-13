# event_type_dao.py
from .general_dao import GeneralDAO
from ..domain import EventType

class EventTypeDAO(GeneralDAO):
    _domain_type = EventType

    def find_all_event_types(self):
        event_types = self.find_all()
        print(f"Found event types: {event_types}")
        return event_types

    def find_event_type_by_id(self, event_type_id):
        return self.find_by_id(event_type_id)

    def create_event_type(self, event_type):
        return self.create(event_type)

    def create_all_event_types(self, event_type_list):
        return self.create_all(event_type_list)

    def update_event_type(self, event_type_id, updated_event_type):
        return self.update(event_type_id, updated_event_type)

    def patch_event_type(self, event_type_id, field_name, value):
        return self.patch(event_type_id, field_name, value)

    def delete_event_type(self, event_type_id):
        return self.delete(event_type_id)

    def delete_all_event_types(self):
        return self.delete_all()
