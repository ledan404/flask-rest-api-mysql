from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import calls_service

class CallsController(GeneralController):
    """
    Controller for Calls table.
    """
    _service = calls_service

    def find_callers(self, caller_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._service.find_callers(caller_id)

    def find_cities(self, city_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._service.find_cities(city_id)

    def __init__(self):
        super().__init__()
