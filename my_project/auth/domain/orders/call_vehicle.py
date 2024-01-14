from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class CallVehicles(db.Model, IDto):
    """
    Model declaration for CallVehicles table.
    """
    __tablename__ = "call_vehicles"

    call_vehicle_id = db.Column(db.Integer, primary_key=True)
    call_id = db.Column(db.Integer, db.ForeignKey("calls.call_id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.vehicle_id"), nullable=False)
    dispatch_time = db.Column(db.Time, nullable=False)
    return_time = db.Column(db.Time, default=None, nullable=True)

    vehicle = db.relationship("Vehicles", back_populates="call_vehicles")

    def __repr__(self) -> str:
        return f"CallVehicles({self.call_vehicle_id}, {self.call_id}, {self.vehicle_id}, {self.dispatch_time}, {self.return_time})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "call_vehicle_id": self.call_vehicle_id,
            "call_id": self.call_id,
            "vehicle_id": self.vehicle_id,
            "dispatch_time": str(self.dispatch_time),
            "return_time": str(self.return_time) if self.return_time else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CallVehicles:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CallVehicles(
            call_id=dto_dict.get("call_id"),
            vehicle_id=dto_dict.get("vehicle_id"),
            dispatch_time=dto_dict.get("dispatch_time"),
            return_time=dto_dict.get("return_time"),
        )
        return obj
