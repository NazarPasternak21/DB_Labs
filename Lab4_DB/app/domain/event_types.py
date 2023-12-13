from typing import Dict, Any
from app import db

class EventType(db.Model):
    __tablename__ = 'event_types'
    Event_Type_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=True)
    Description = db.Column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return f"EventType(Event_Type_ID={self.Event_Type_ID}, Name='{self.Name}', Description='{self.Description}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Event_Type_ID': self.Event_Type_ID,
            'Name': self.Name,
            'Description': self.Description
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'EventType':
        return EventType(
            Name=data.get('Name'),
            Description=data.get('Description')
        )
