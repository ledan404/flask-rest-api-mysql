from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import rescuer_service

class RescuersController(GeneralController):
    """
    Controller for Rescuers table.
    """
    _service = rescuer_service

    def __init__(self):
        super().__init__()
