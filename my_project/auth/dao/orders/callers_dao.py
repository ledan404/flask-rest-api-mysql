from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Callers


class CallersDAO(GeneralDAO):
    """
    Realisation of Callers data access layer.
    """

    _domain_type = Callers
