from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Injuries


class InjuriesDAO(GeneralDAO):
    """
    Data Access Object for the Injuries table.
    """
    _domain_type = Injuries