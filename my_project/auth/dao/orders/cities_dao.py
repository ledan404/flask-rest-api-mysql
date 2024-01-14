from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Cities


class CitiesDAO(GeneralDAO):
    """
    Realisation of Cities data access layer.
    """

    _domain_type = Cities
