import sqlalchemy

from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Cities


class CitiesDAO(GeneralDAO):
    """
    Realisation of Cities data access layer.
    """

    _domain_type = Cities

    def procedure_insert_cities(self, city_name):
        try:
            result = self._session.execute(sqlalchemy.text("CALL InsertCity(:p1)"),
                                           {"p1": city_name })
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
