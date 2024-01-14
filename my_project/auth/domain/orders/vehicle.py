from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Vehicles(db.Model, IDto):
    """
    Model declaration for Vehicles table.
    """
    __tablename__ = "vehicles"

    vehicle_id = db.Column(db.Integer, primary_key=True, )
    vehicle_name = db.Column(db.String(255), nullable=False)

    call_vehicles = db.relationship("CallVehicles", back_populates="vehicle")

    def __repr__(self) -> str:
        return f"Vehicles({self.vehicle_id}, '{self.vehicle_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "vehicle_id": self.vehicle_id,
            "vehicle_name": self.vehicle_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Vehicles:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Vehicles(
            vehicle_name=dto_dict.get("vehicle_name"),
        )
        return obj
