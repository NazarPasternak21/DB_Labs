from typing import Dict, Any
from app import db

class Employee(db.Model):
    __tablename__ = 'employees'
    Employee_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=True)
    Age = db.Column(db.Integer, nullable=True)
    Phone = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(255), nullable=True)
    Employee_Type = db.Column(db.String(50), nullable=True)
    Order_ID = db.Column(db.Integer, db.ForeignKey('orders.Order_ID'), nullable=True)

    def __repr__(self) -> str:
        return f"Employee(Employee_ID={self.Employee_ID}, Name='{self.Name}', Age={self.Age}, Phone='{self.Phone}', Email='{self.Email}', Employee_Type='{self.Employee_Type}', Order_ID={self.Order_ID})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Employee_ID': self.Employee_ID,
            'Name': self.Name,
            'Age': self.Age,
            'Phone': self.Phone,
            'Email': self.Email,
            'Employee_Type': self.Employee_Type,
            'Order_ID': self.Order_ID
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Employee':
        return Employee(
            Name=data.get('Name'),
            Age=data.get('Age'),
            Phone=data.get('Phone'),
            Email=data.get('Email'),
            Employee_Type=data.get('Employee_Type'),
            Order_ID=data.get('Order_ID')
        )
