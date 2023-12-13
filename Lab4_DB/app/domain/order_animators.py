from typing import Dict, Any
from app import db

class OrderAnimator(db.Model):
    __tablename__ = 'order_animators'
    Order_Animator_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Order_ID = db.Column(db.Integer, db.ForeignKey('orders.Order_ID'), nullable=True)
    Animator_ID = db.Column(db.Integer, db.ForeignKey('animators.Animator_ID'), nullable=True)

    def __repr__(self) -> str:
        return f"OrderAnimator(Order_Animator_ID={self.Order_Animator_ID}, Order_ID={self.Order_ID}, Animator_ID={self.Animator_ID})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Order_Animator_ID': self.Order_Animator_ID,
            'Order_ID': self.Order_ID,
            'Animator_ID': self.Animator_ID
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'OrderAnimator':
        return OrderAnimator(
            Order_ID=data.get('Order_ID'),
            Animator_ID=data.get('Animator_ID')
        )
