from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Calls
from my_project.auth.domain import Callers
from my_project.auth.domain.orders.cities import Cities


class CallsDAO(GeneralDAO):
    """
    Realisation of Calls data access layer.
    """

    _domain_type = Calls

    def find_callers(self, caller_id: int):
        """
        Find calls along with their callers for a specific caller_id.
        :param caller_id: ID of the caller
        :return: List of calls with caller information for the specified caller_id
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self._session

        # Query the Calls table along with the associated Caller information
        calls_with_caller = (
            session.query(Calls, Callers)
            .join(Callers, Calls.caller_id == Callers.caller_id)
            .filter(Calls.caller_id == caller_id)
            .all()
        )

        # Extract information from the result
        calls_data = [
            {
                "calls" : {
                    "call_id": call.call_id,
                    "caller_id": call.caller_id,
                    "city_id": call.city_id,
                    "phone_number": call.phone_number,
                    "short_description": call.short_description,
                    "detailed_description": call.detailed_description,
                    "call_address": call.call_address,
                    "call_date": call.call_date.isoformat(),
                    "call_time": call.call_time.strftime("%H:%M:%S"),
                },
                 "caller" : {
                    "caller_id": caller.caller_id,
                    "caller_name": caller.caller_name
                }
            }
            for call, caller in calls_with_caller
        ]

        return calls_data

    def find_cities(self, city_id):
        """
        Find calls along with their cities for a specific city_id.
        :param city_id: ID of the city
        :return: List of calls with city information for the specified city_id
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self._session

        # Query the Calls table along with the associated City information
        calls_with_city = (
            session.query(Calls, Cities)
            .join(Cities, Calls.city_id == Cities.city_id)
            .filter(Calls.city_id == city_id)
            .all()
        )

        # Extract information from the result
        calls_data = [
            {
                "calls" : {
                    "call_id": call.call_id,
                    "caller_id": call.caller_id,
                    "city_id": call.city_id,
                    "phone_number": call.phone_number,
                    "short_description": call.short_description,
                    "detailed_description": call.detailed_description,
                    "call_address": call.call_address,
                    "call_date": call.call_date.isoformat(),
                    "call_time": call.call_time.strftime("%H:%M:%S"),
                },
                 "city" : {
                    "city_id": city.city_id,
                    "city_name": city.city_name
                }
            }
            for call, city in calls_with_city
        ]

        return calls_data