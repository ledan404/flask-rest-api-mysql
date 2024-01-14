from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Calls


class CallsDAO(GeneralDAO):
    """
    Realisation of Calls data access layer.
    """

    _domain_type = Calls
