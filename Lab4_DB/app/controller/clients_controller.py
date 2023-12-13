# client_controller.py
from .general_controller import GeneralController
from ..service import clients_service

class ClientController(GeneralController):
    _service = clients_service.ClientService()
    def find_all_clients(self):
        return self.find_all()

    def find_client_by_id(self, key):
        return self.find_by_id(key)

    def create_client(self, client):
        return self.create(client)

    def create_all_clients(self, client_list):
        return self.create_all(client_list)

    def update_client(self, key, new_client):
        return self.update(key, new_client)

    def patch_client(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_client(self, key):
        return self.delete(key)

    def delete_all_clients(self):
        return self.delete_all()
