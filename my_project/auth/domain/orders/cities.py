from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Cities(db.Model, IDto):
    """
    Model declaration for Cities table.
    """
    __tablename__ = "cities"

    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(255), nullable=False)

    calls = db.relationship('Calls', back_populates='city_rel', lazy=True)

    def __repr__(self) -> str:
        return f"Cities({self.city_id}, '{self.city_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts the domain object into DTO without relationship.
        :return: DTO object as a dictionary
        """
        return {
            "city_id": self.city_id,
            "city_name": self.city_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Cities:
        """
        Creates a domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Cities(
            city_name=dto_dict.get("city_name"),
        )
        return obj
