from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import calls_service

class CallsController(GeneralController):
    """
    Controller for Calls table.
    """
    _service = calls_service

    def __init__(self):
        super().__init__()
