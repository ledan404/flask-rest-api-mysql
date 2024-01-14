from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import emergency_reason_service

class EmergencyReasonController(GeneralController):
    """
    Realisation of EmergencyReason controller.
    """
    _service = emergency_reason_service
