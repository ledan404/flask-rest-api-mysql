from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import CallVehicles
from sqlalchemy.orm import joinedload

from my_project.auth.domain.orders.calls import Calls
from my_project.auth.domain.orders.vehicle import Vehicles


class CallVehiclesDAO(GeneralDAO):
    """
    Realisation of CallVehicles data access layer.
    """

    _domain_type = CallVehicles

    def find_vehicles_for_call(self, call_id: int):
        """
        Find vehicles associated with a specific call along with call information.
        :param call_id: ID of the call
        :return: JSON response of vehicles with call information for the specified call_id
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self._session

        # Query the CallVehicles table along with the associated Call and Vehicle information
        vehicles_for_call = (
            session.query(CallVehicles, Calls, Vehicles)
            .join(Calls, CallVehicles.call_id == Calls.call_id)
            .join(Vehicles, CallVehicles.vehicle_id == Vehicles.vehicle_id)
            .filter(CallVehicles.call_id == call_id)
            .all()
        )

        # Extract information from the result
        vehicles_data = [
            {
                "call_vehicle_id": call_vehicle.call_vehicle_id,
                "call_id": call.call_id,
                "vehicle_id": vehicle.vehicle_id,
                "dispatch_time": call_vehicle.dispatch_time.strftime("%H:%M:%S"),
                "return_time": call_vehicle.return_time.strftime("%H:%M:%S")
                if call_vehicle.return_time
                else None,
                "call": {
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
                "vehicle": {
                    "vehicle_id": vehicle.vehicle_id,
                    "vehicle_name": vehicle.vehicle_name,

                },
            }
            for call_vehicle, call, vehicle in vehicles_for_call
        ]
        return vehicles_data