from .orders.call_vehicle_service import CallVehiclesService
from .orders.callers_services import CallersService
from .orders.calls_services import CallsService
from .orders.cities_services import CitiesService
from .orders.emergency_reason_services import EmergencyReasonService
from .orders.injuries_sevices import InjuriesService
from .orders.recscuer_call_services import RescuerCallsService
from .orders.rescuer_service import RescuersService
from .orders.vehicle_services import VehiclesService

emergency_reason_service = EmergencyReasonService()
calls_service = CallsService()
call_vehicle_service = CallVehiclesService()
vehicles_service = VehiclesService()
rescuer_service = RescuersService()
rescuer_call_service = RescuerCallsService()
cities_service = CitiesService()
callers_service = CallersService()
injuries_service = InjuriesService()
