from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import emergency_reason_dao

class EmergencyReasonService(GeneralService):
    """
    Realisation of EmergencyReason service.
    """
    _dao = emergency_reason_dao