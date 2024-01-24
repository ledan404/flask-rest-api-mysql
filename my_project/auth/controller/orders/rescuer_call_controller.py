from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import rescuer_call_service

class RescuerCallsController(GeneralController):
    """
    Controller for RescuerCalls table.
    """
    _service = rescuer_call_service

    def find_rescuers(self, rescuers_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._service.find_rescuers(rescuers_id)

    def __init__(self):
        super().__init__()
