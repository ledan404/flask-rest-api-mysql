from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import RescuerCalls


class RescuerCallsDAO(GeneralDAO):
    """
    Realisation of RescuerCalls data access layer.
    """

    _domain_type = RescuerCalls
