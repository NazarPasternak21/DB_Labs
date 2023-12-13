# client_dao.py
from .general_dao import GeneralDAO
from ..domain import Client

class ClientDAO(GeneralDAO):
    _domain_type = Client

    def find_all_clients(self):
        clients = self.find_all()
        print(f"Found clients: {clients}")
        return clients

    def find_client_by_id(self, client_id):
        return self.find_by_id(client_id)

    def create_client(self, client):
        return self.create(client)

    def create_all_clients(self, client_list):
        return self.create_all(client_list)

    def update_client(self, client_id, updated_client):
        return self.update(client_id, updated_client)

    def patch_client(self, client_id, field_name, value):
        return self.patch(client_id, field_name, value)

    def delete_client(self, client_id):
        return self.delete(client_id)

    def delete_all_clients(self):
        return self.delete_all()
