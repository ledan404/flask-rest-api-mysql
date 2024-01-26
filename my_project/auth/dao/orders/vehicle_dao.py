from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Vehicles


class VehiclesDAO(GeneralDAO):
    """
    Realisation of Vehicles data access layer.
    """

    _domain_type = Vehicles
