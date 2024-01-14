from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import cities_service

class CitiesController(GeneralController):
    """
    Controller for Cities table.
    """
    _service = cities_service

    def __init__(self):
        super().__init__()
