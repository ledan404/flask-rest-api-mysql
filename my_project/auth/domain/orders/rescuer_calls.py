from typing import Dict, Any
from my_project import db
from datetime import time

class RescuerCalls(db.Model):
    """
    Model declaration for RescuerCalls table.
    """
    __tablename__ = "rescuer_calls"

    rescuer_call_id = db.Column(db.Integer, primary_key=True)
    call_id = db.Column(db.Integer, db.ForeignKey("calls.call_id"), nullable=False)
    rescuer_id = db.Column(db.Integer, db.ForeignKey("rescuers.rescuer_id"), nullable=False)
    dispatch_time = db.Column(db.Time, nullable=False)
    return_time = db.Column(db.Time, default=None, nullable=True)

    call = db.relationship("Calls", back_populates="rescuer_calls")
    rescuer = db.relationship("Rescuers", back_populates="rescuer_calls")


    def __repr__(self) -> str:
        return (f"RescuerCalls({self.rescuer_call_id}, {self.call_id}, {self.rescuer_id}, "
                f"'{self.dispatch_time}', '{self.return_time}')")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationships.
        :return: DTO object as dictionary
        """
        return {
            "rescuer_call_id": self.rescuer_call_id,
            "call_id": self.call_id,
            "rescuer_id": self.rescuer_id,
            "dispatch_time": self.dispatch_time.strftime('%H:%M:%S'),
            "return_time": self.return_time.strftime('%H:%M:%S') if self.return_time else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'RescuerCalls':
        """
        Creates domain object from DTO.
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = RescuerCalls(
            call_id=dto_dict.get("call_id"),
            rescuer_id=dto_dict.get("rescuer_id"),
            dispatch_time=time.fromisoformat(dto_dict.get("dispatch_time")),
            return_time=time.fromisoformat(dto_dict.get("return_time")) if dto_dict.get("return_time") else None,
        )
        return obj
