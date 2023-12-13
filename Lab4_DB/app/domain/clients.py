from typing import Dict, Any
from app import db

class Client(db.Model):
    __tablename__ = 'clients'
    Client_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=True)
    Phone = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(255), nullable=True)
    Address = db.Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return f"Client(Client_ID={self.Client_ID}, Name='{self.Name}', Phone='{self.Phone}', Email='{self.Email}', Address='{self.Address}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Client_ID': self.Client_ID,
            'Name': self.Name,
            'Phone': self.Phone,
            'Email': self.Email,
            'Address': self.Address
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Client':
        return Client(
            Name=data.get('Name'),
            Phone=data.get('Phone'),
            Email=data.get('Email'),
            Address=data.get('Address')
        )
