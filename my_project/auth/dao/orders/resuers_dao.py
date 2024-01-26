from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Rescuers


class RescuersDAO(GeneralDAO):
    _domain_type = Rescuers
