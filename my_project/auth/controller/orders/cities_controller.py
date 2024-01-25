from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import cities_service

class CitiesController(GeneralController):
    """
    Controller for Cities table.
    """
    _service = cities_service

    def procedure_insert_cities(self, city_name: str):
        self._service.procedure_insert_cities(city_name)

    def __init__(self):
        super().__init__()
