from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Callers(db.Model, IDto):
    """
    Model declaration for Callers table.
    """
    __tablename__ = "callers"

    caller_id = db.Column(db.Integer, primary_key=True)
    caller_name = db.Column(db.String(255), nullable=False)

    calls = db.relationship('Calls', back_populates='caller_rel', lazy=True)

    def __repr__(self) -> str:
        return f"Callers({self.caller_id}, '{self.caller_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "caller_id": self.caller_id,
            "caller_name": self.caller_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Callers':
        obj = Callers(
            caller_name=dto_dict.get("caller_name"),
        )
        return obj