from my_project.auth.dao import vehicles_dao
from my_project.auth.service.general_service import GeneralService


class VehiclesService(GeneralService):
    """
    Realisation of Vehicles service.
    """

    _dao = vehicles_dao

    def insert_data(self):
        return self._dao.insert_data()