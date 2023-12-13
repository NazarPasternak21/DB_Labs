from typing import Dict, Any
from app import db

class Agency(db.Model):
    __tablename__ = 'agencies'
    Agency_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=True)
    Address = db.Column(db.String(255), nullable=True)
    Contact_Info = db.Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return f"Agency(Agency_ID={self.Agency_ID}, Name='{self.Name}', Address='{self.Address}', Contact_Info='{self.Contact_Info}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Agency_ID': self.Agency_ID,
            'Name': self.Name,
            'Address': self.Address,
            'Contact_Info': self.Contact_Info
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Agency':
        return Agency(
            Name=data.get('Name'),
            Address=data.get('Address'),
            Contact_Info=data.get('Contact_Info')
        )
