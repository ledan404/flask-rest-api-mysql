from my_project.auth.dao import callers_dao
from my_project.auth.service.general_service import GeneralService


class CallersService(GeneralService):
    """
    Realization of Callers service.
    """

    _dao = callers_dao
