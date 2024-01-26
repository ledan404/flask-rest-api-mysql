from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class EmergencyReasons(db.Model, IDto):
    """
    Model declaration for EmergencyReasons table.
    """
    __tablename__ = "emergency_reasons"

    emergency_reason_id = db.Column(db.Integer, primary_key=True)
    call_id = db.Column(db.Integer, nullable=False)
    reason_description = db.Column(db.Text, default=None, nullable=True)


    def __repr__(self) -> str:
        return f"EmergencyReasons({self.emergency_reason_id}, {self.call_id}, {self.reason_description})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "emergency_reason_id": self.emergency_reason_id,
            "call_id": self.call_id,
            "reason_description": self.reason_description,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmergencyReasons:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = EmergencyReasons(
            call_id=dto_dict.get("call_id"),
            reason_description=dto_dict.get("reason_description"),
        )
        return obj
