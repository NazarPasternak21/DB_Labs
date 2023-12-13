# agency_controller.py
# agencies_controller.py
from .general_controller import GeneralController
from ..service import agencies_service

class AgencyController(GeneralController):
    _service = agencies_service.AgenciesService()

    def find_all_agencies(self):
        return self.find_all()

    def find_agency_by_id(self, key):
        return self.find_by_id(key)

    def create_agency(self, agency):
        return self.create(agency)

    def create_all_agencies(self, agency_list):
        return self.create_all(agency_list)

    def update_agency(self, key, new_agency):
        return self.update(key, new_agency)

    def patch_agency(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_agency(self, key):
        return self.delete(key)

    def delete_all_agencies(self):
        return self.delete_all()
