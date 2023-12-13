from typing import Dict, Any
from app import db

class Animator(db.Model):
    __tablename__ = 'animators'
    Animator_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=True)
    Age = db.Column(db.Integer, nullable=True)
    Phone = db.Column(db.String(20), nullable=True)

    def __repr__(self) -> str:
        return f"Animator(Animator_ID={self.Animator_ID}, Name='{self.Name}', Age={self.Age}, Phone='{self.Phone}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Animator_ID': self.Animator_ID,
            'Name': self.Name,
            'Age': self.Age,
            'Phone': self.Phone
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Animator':
        return Animator(
            Name=data.get('Name'),
            Age=data.get('Age'),
            Phone=data.get('Phone')
        )
