
# orders DB
from .orders.emergency_reason_dao import EmergencyReasonsDAO
from .orders.injuries_dao import InjuriesDAO
from .orders.rescuer_call_dao import RescuerCallsDAO
from .orders.resuers_dao import RescuersDAO
from .orders.call_vehicle_dao import CallVehiclesDAO
from .orders.vehicle_dao import VehiclesDAO
from .orders.cities_dao import CitiesDAO
from .orders.calls_dao import CallsDAO
from .orders.callers_dao import CallersDAO

emergency_reason_dao = EmergencyReasonsDAO()
injuries_dao = InjuriesDAO()
rescuer_call_dao = RescuerCallsDAO()
rescuers_dao = RescuersDAO()
call_vehicle_dao = CallVehiclesDAO()
vehicles_dao = VehiclesDAO()
cities_dao = CitiesDAO()
calls_dao = CallsDAO()
callers_dao = CallersDAO()
