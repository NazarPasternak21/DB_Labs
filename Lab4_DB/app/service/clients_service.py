# client_service.py
from .general_service import GeneralService
from ..dao import clients_dao

class ClientService(GeneralService):
    _dao = clients_dao

    def find_all(self):
        return self._dao.find_all_clients()

    def find_all_clients(self):
        return self._dao.find_all_clients()

    def find_client_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_client(self, client):
        return self._dao.create(client)

    def create_all_clients(self, client_list):
        return self._dao.create_all(client_list)

    def update_client(self, key, new_client):
        return self._dao.update(key, new_client)

    def patch_client(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_client(self, key):
        return self._dao.delete(key)

    def delete_all_clients(self):
        return self._dao.delete_all()
