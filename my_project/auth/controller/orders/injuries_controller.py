from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import injuries_service

class InjuriesController(GeneralController):
    """
    Controller for Injuries table.
    """
    _service = injuries_service

