from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import EmergencyReasons

class EmergencyReasonsDAO(GeneralDAO):
    """
    Realisation of EmergencyReasons data access layer.
    """
    _domain_type = EmergencyReasons
