from my_project.auth.dao import injuries_dao
from my_project.auth.service.general_service import GeneralService


class InjuriesService(GeneralService):
    """
    Realisation of Injuries service.
    """
    _dao = injuries_dao
