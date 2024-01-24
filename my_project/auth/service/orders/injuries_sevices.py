from my_project.auth.dao import injuries_dao
from my_project.auth.service.general_service import GeneralService


class InjuriesService(GeneralService):
    """
    Realisation of Injuries service.
    """
    _dao = injuries_dao

    def find_injuries(self, call_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._dao.find_injuries(call_id)
    def find_rescuer(self, rescuer_id: int):
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._dao.find_rescuer(rescuer_id)