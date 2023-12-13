from typing import Dict, Any
from app import db

class AnimatorOrder(db.Model):
    __tablename__ = 'animator_orders'
    Animator_Order_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Animator_ID = db.Column(db.Integer, db.ForeignKey('animators.Animator_ID'), nullable=True)
    Order_ID = db.Column(db.Integer, db.ForeignKey('orders.Order_ID'), nullable=True)

    def __repr__(self) -> str:
        return f"AnimatorOrder(Animator_Order_ID={self.Animator_Order_ID}, Animator_ID={self.Animator_ID}, Order_ID={self.Order_ID})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Animator_Order_ID': self.Animator_Order_ID,
            'Animator_ID': self.Animator_ID,
            'Order_ID': self.Order_ID
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'AnimatorOrder':
        return AnimatorOrder(
            Animator_ID=data.get('Animator_ID'),
            Order_ID=data.get('Order_ID')
        )
