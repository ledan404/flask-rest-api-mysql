from typing import Dict, Any
from datetime import date, time

from my_project import db

class Calls(db.Model):
    """
    Model declaration for Calls table.
    """
    __tablename__ = "calls"

    call_id = db.Column(db.Integer, primary_key=True,)
    caller_id = db.Column(db.Integer, db.ForeignKey('callers.caller_id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))
    phone_number = db.Column(db.String(20))
    short_description = db.Column(db.Text)
    detailed_description = db.Column(db.Text, default=None, nullable=True)
    call_address = db.Column(db.String(255))
    call_date = db.Column(db.Date)
    call_time = db.Column(db.Time)

    city_rel = db.relationship('Cities', back_populates='calls')
    caller_rel = db.relationship('Callers', back_populates='calls', lazy=True)
    rescuer_calls = db.relationship('RescuerCalls', back_populates='call')
    injuries = db.relationship('Injuries', back_populates='call_rel')


    def __repr__(self) -> str:
        return (f"Calls({self.call_id}, {self.caller_id}, {self.city_id}, {self.emergency_type_id}, "
                f"'{self.phone_number}', '{self.short_description}', '{self.detailed_description}', "
                f"'{self.call_address}', {self.call_date}, {self.call_time})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "call_id": self.call_id,
            "caller_id": self.caller_id,
            "city_id": self.city_id,
            "phone_number": self.phone_number,
            "short_description": self.short_description,
            "detailed_description": self.detailed_description,
            "call_address": self.call_address,
            "call_date": self.call_date.isoformat(),
            "call_time": self.call_time.strftime('%H:%M:%S'),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Calls':
        obj = Calls(
            caller_id=dto_dict.get("caller_id"),
            city_id=dto_dict.get("city_id"),
            phone_number=dto_dict.get("phone_number"),
            short_description=dto_dict.get("short_description"),
            detailed_description=dto_dict.get("detailed_description"),
            call_address=dto_dict.get("call_address"),
            call_date=date.fromisoformat(dto_dict.get("call_date")),
            call_time=time.fromisoformat(dto_dict.get("call_time")),
        )
        return obj