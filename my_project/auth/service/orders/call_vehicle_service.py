from my_project.auth.dao import call_vehicle_dao
from my_project.auth.service.general_service import GeneralService


class CallVehiclesService(GeneralService):
    """
    Realisation of CallVehicles service.
    """

    _dao = call_vehicle_dao

    def find_vehicles_for_call(self, call_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._dao.find_vehicles_for_call(call_id)