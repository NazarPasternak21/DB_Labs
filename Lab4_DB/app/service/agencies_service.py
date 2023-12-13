from .general_service import GeneralService
from ..dao import agencies_dao

class AgenciesService(GeneralService):
    _dao = agencies_dao

    def find_all(self):
        return self._dao.find_all_agencies()

    def find_all_agencies(self):
        return self._dao.find_all_agencies()

    def find_agency_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_agency(self, agency):
        return self._dao.create(agency)

    def create_all_agencies(self, agency_list):
        return self._dao.create_all(agency_list)

    def update_agency(self, key, new_agency):
        return self._dao.update(key, new_agency)

    def patch_agency(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_agency(self, key):
        return self._dao.delete(key)

    def delete_all_agencies(self):
        return self._dao.delete_all()
