from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import RescuerCalls
from my_project.auth.domain.orders.rescuers import Rescuers


class RescuerCallsDAO(GeneralDAO):
    """
    Realisation of RescuerCalls data access layer.
    """

    _domain_type = RescuerCalls

    def find_rescuers(self, rescuers_id: int):
        """
        Find all rescuers by rescuers_id in rescuer table
        """
        session = self._session

        rescuers_in_rescuercall = (
            session.query(RescuerCalls, Rescuers)
            .join(RescuerCalls, Rescuers.rescuer_id == Rescuers.rescuer_id)
            .filter(RescuerCalls.rescuer_id == rescuers_id)
            .all()
        )
        rescuers_data = [
            {
                "rescuer_id": rescuer.rescuer_id,
                "call_id": rescuer_calls.call_id,
                "dispatch_time": rescuer_calls.dispatch_time.strftime("%H:%M:%S"),
                "return_time": rescuer_calls.return_time.strftime("%H:%M:%S"),
                "rescuer": {
                    "rescuer_id": rescuer.rescuer_id,
                    "rescuer_name": rescuer.rescuer_name
                }
            }
            for rescuer_calls, rescuer in rescuers_in_rescuercall
        ]

        return rescuers_data