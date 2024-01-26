from __future__ import annotations
from typing import Dict, Any

from my_project import db



class Injuries(db.Model):
    """
    Model declaration for Injuries table.
    """
    __tablename__ = "injuries"

    injury_id = db.Column(db.Integer, primary_key=True)
    call_id = db.Column(db.Integer, db.ForeignKey('calls.call_id'), nullable=True)
    rescuer_id = db.Column(db.Integer, db.ForeignKey('rescuers.rescuer_id'), nullable=False)
    description = db.Column(db.Text, default=None, nullable=True)
    hospital = db.Column(db.String(255), default=None, nullable=True)
    diagnosis = db.Column(db.Text, default=None, nullable=True)

    call_rel = db.relationship('Calls', back_populates='injuries')
    rescuer_rel = db.relationship('Rescuers', back_populates='injuries')

    def __repr__(self) -> str:
        return (f"Injuries({self.injury_id}, {self.call_id}, {self.rescuer_id}, "
                f"'{self.description}', '{self.hospital}', '{self.diagnosis}')")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationships.
        :return: DTO object as dictionary
        """
        return {
            "injury_id": self.injury_id,
            "call_id": self.call_id,
            "rescuer_id": self.rescuer_id,
            "description": self.description,
            "hospital": self.hospital,
            "diagnosis": self.diagnosis,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Injuries':
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Injuries(
            call_id=dto_dict.get("call_id"),
            rescuer_id=dto_dict.get("rescuer_id"),
            description=dto_dict.get("description"),
            hospital=dto_dict.get("hospital"),
            diagnosis=dto_dict.get("diagnosis"),
        )
        return obj
