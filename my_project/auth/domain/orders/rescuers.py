from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Rescuers(db.Model, IDto):
    """
    Model declaration for Rescuers table.
    """
    __tablename__ = "rescuers"

    rescuer_id = db.Column(db.Integer, primary_key=True)
    rescuer_name = db.Column(db.String(255), nullable=False)

    rescuer_calls = db.relationship('RescuerCalls', back_populates='rescuer')
    injuries = db.relationship('Injuries', back_populates='rescuer_rel')
    def __repr__(self) -> str:
        return f"Rescuers({self.rescuer_id}, '{self.rescuer_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "rescuer_id": self.rescuer_id,
            "rescuer_name": self.rescuer_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Rescuers:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Rescuers(
            rescuer_name=dto_dict.get("rescuer_name"),
        )
        return obj
