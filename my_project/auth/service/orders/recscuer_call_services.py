from my_project.auth.dao import rescuer_call_dao
from my_project.auth.service.general_service import GeneralService


class RescuerCallsService(GeneralService):
    """
    Realisation of RescuerCalls service.
    """

    _dao = rescuer_call_dao
