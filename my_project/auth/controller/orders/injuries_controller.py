from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import injuries_service

class InjuriesController(GeneralController):
    """
    Controller for Injuries table.
    """
    _service = injuries_service

    def find_injuries(self, call_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._service.find_injuries(call_id)
    def find_rescuer(self, rescuer_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._service.find_rescuer(rescuer_id)

