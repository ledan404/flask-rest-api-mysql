from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import call_vehicle_service

class CallVehiclesController(GeneralController):
    """
    Controller for CallVehicles table.
    """
    _service = call_vehicle_service

    def find_vehicles_for_call(self, call_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._service.find_vehicles_for_call(call_id)

    def __init__(self):
        super().__init__()
