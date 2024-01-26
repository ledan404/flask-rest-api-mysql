from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Injuries
from my_project.auth.domain.orders import calls
from my_project.auth.domain.orders.calls import Calls
from my_project.auth.domain.orders.rescuers import Rescuers


class InjuriesDAO(GeneralDAO):
    """
    Data Access Object for the Injuries table.
    """

    _domain_type = Injuries

    def find_injuries(self, call_id: int):
        """
        Find all injuries by call_id in Injuries table
        """
        session = self._session

        injuries_for_call = (
            session.query(Injuries, Calls)
            .join(Calls, Injuries.call_id == Calls.call_id)
            .filter(Injuries.call_id == call_id)
            .all()
        )
        injuries_data = [
            {
                "injury_id": injury.injury_id,
                "call_id": injury.call_id,
                "rescuer_id": injury.rescuer_id,
                "injury_description": injury.description,
                "hospital": injury.hospital,
                "diagnostic": injury.diagnosis,
                "calls": {
                    "call_id": calls.call_id,
                    "caller_id": calls.caller_id,
                    "city_id": calls.city_id,
                    "phone_number": calls.phone_number,
                    "short_description": calls.short_description,
                    "detailed_description": calls.detailed_description,
                    "call_address": calls.call_address,
                    "call_date": calls.call_date.isoformat(),
                    "call_time": calls.call_time.strftime("%H:%M:%S"),
                },
            }
            for injury, calls in injuries_for_call
        ]

        return injuries_data

    def find_rescuer(self, rescuer_id: int):
        """
        Find all rescuers by rescuer_id in rescuer table
        """
        session = self._session

        rescuer_in_rescuer = (
            session.query(Injuries, Rescuers)
            .join(Rescuers, Injuries.rescuer_id == Rescuers.rescuer_id)
            .filter(Injuries.rescuer_id == rescuer_id)
            .all()
            # session.query(Rescuers).filter(Rescuers.rescuer_id == rescuer_id).all()
        )
        rescuer_data = [
            {
                "injury": {
                        "injury_id": injury.injury_id,
                        "call_id": injury.call_id,
                        "rescuer_id": injury.rescuer_id,
                        "injury_description": injury.description,
                        "hospital": injury.hospital,
                        "diagnostic": injury.diagnosis,
                },
                "rescuer": {
                    "rescuer_id": rescuer.rescuer_id,
                    "rescuer_name": rescuer.rescuer_name,
                },
            }
            for injury, rescuer in rescuer_in_rescuer
        ]

        return rescuer_data
