from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import callers_service

class CallersController(GeneralController):
    """
    Controller for Callers table.
    """
    _service = callers_service

    def make_operation(self):
        return self._service.make_operation()

    def __init__(self):
        super().__init__()
