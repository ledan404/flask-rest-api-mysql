from typing import List

from my_project.auth.dao import calls_dao
from my_project.auth.service.general_service import GeneralService


class CallsService(GeneralService):
    """
    Realisation of Calls service.
    """

    _dao = calls_dao

    def find_callers(self, caller_id: int) -> List[dict]:
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._dao.find_callers(caller_id)

    def find_cities(self, city_id: int) -> List[dict]:
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._dao.find_cities(city_id)
