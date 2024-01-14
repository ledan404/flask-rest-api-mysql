from my_project.auth.dao import cities_dao
from my_project.auth.service.general_service import GeneralService


class CitiesService(GeneralService):
    """
    Realisation of Cities service.
    """

    _dao = cities_dao
