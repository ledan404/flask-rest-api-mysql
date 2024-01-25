from my_project.auth.dao import cities_dao
from my_project.auth.dao.orders.cities_dao import CitiesDAO
from my_project.auth.service.general_service import GeneralService


class CitiesService(GeneralService):
    """
    Realisation of Cities service.
    """

    _dao = cities_dao

    def procedure_insert_cities(self, city_name: str):
        self._dao.procedure_insert_cities(city_name)
