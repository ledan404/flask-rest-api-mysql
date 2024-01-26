from my_project.auth.dao import vehicles_dao
from my_project.auth.service.general_service import GeneralService


class VehiclesService(GeneralService):
    """
    Realisation of Vehicles service.
    """

    _dao = vehicles_dao
