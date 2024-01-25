from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import vehicles_service

class VehiclesController(GeneralController):
    """
    Controller for Vehicles table.
    """
    _service = vehicles_service

    def insert_data(self):
        return self._service.insert_data()

    def __init__(self):
        super().__init__()
