import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Vehicles


class VehiclesDAO(GeneralDAO):
    """
    Realisation of Vehicles data access layer.
    """

    _domain_type = Vehicles

    def insert_data(self):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL InsertVehicles();")
            )
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
