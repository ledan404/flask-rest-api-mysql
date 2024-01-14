from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import CallVehicles


class CallVehiclesDAO(GeneralDAO):
    """
    Realisation of CallVehicles data access layer.
    """

    _domain_type = CallVehicles
