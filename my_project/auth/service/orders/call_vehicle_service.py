from my_project.auth.dao import call_vehicle_dao
from my_project.auth.service.general_service import GeneralService


class CallVehiclesService(GeneralService):
    """
    Realisation of CallVehicles service.
    """

    _dao = call_vehicle_dao
