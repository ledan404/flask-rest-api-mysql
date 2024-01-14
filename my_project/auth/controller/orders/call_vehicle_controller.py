from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import call_vehicle_service

class CallVehiclesController(GeneralController):
    """
    Controller for CallVehicles table.
    """
    _service = call_vehicle_service

    def __init__(self):
        super().__init__()
