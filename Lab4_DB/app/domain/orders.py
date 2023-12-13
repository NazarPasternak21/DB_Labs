from typing import Dict, Any
from app import db

class Order(db.Model):
    __tablename__ = 'orders'
    Order_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date = db.Column(db.Date, nullable=True)
    Duration = db.Column(db.Integer, nullable=True)
    Event_Address = db.Column(db.String(255), nullable=True)
    Cost = db.Column(db.DECIMAL(10,2), nullable=True)
    Event_Type_ID = db.Column(db.Integer, db.ForeignKey('event_types.Event_Type_ID'), nullable=True)
    Agency_ID = db.Column(db.Integer, db.ForeignKey('agencies.Agency_ID'), nullable=True)

    def __repr__(self) -> str:
        return f"Order(Order_ID={self.Order_ID}, Date='{self.Date}', Duration={self.Duration}, Event_Address='{self.Event_Address}', Cost={self.Cost}, Event_Type_ID={self.Event_Type_ID}, Agency_ID={self.Agency_ID}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Order_ID': self.Order_ID,
            'Date': str(self.Date),
            'Duration': self.Duration,
            'Event_Address': self.Event_Address,
            'Cost': float(self.Cost) if self.Cost is not None else None,
            'Event_Type_ID': self.Event_Type_ID,
            'Agency_ID': self.Agency_ID
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Order':
        return Order(
            Date=data.get('Date'),
            Duration=data.get('Duration'),
            Event_Address=data.get('Event_Address'),
            Cost=data.get('Cost'),
            Event_Type_ID=data.get('Event_Type_ID'),
            Agency_ID=data.get('Agency_ID')
        )
