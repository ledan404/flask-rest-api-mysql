from my_project.auth.dao import calls_dao
from my_project.auth.service.general_service import GeneralService


class CallsService(GeneralService):
    """
    Realisation of Calls service.
    """

    _dao = calls_dao
