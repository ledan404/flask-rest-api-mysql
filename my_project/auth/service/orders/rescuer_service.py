from my_project.auth.dao import rescuers_dao
from my_project.auth.service.general_service import GeneralService


class RescuersService(GeneralService):
    """
    Realisation of Rescuers service.
    """

    _dao = rescuers_dao
