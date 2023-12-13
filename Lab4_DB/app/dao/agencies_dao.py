from .general_dao import GeneralDAO
from ..domain import Agency


class AgencyDAO(GeneralDAO):
    _domain_type = Agency

    def find_all_agencies(self):
        agencies = self.find_all()
        print(f"Found agencies: {agencies}")
        return agencies

    def find_agency_by_id(self, agency_id):
        return self.find_by_id(agency_id)

    def create_agency(self, agency):
        return self.create(agency)

    def create_all_agencies(self, agency_list):
        return self.create_all(agency_list)

    def update_agency(self, agency_id, updated_agency):
        return self.update(agency_id, updated_agency)

    def patch_agency(self, agency_id, field_name, value):
        return self.patch(agency_id, field_name, value)

    def delete_agency(self, agency_id):
        return self.delete(agency_id)

    def delete_all_agencies(self):
        return self.delete_all()
