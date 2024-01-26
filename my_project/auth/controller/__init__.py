from .orders.call_vehicle_controller import CallVehiclesController
from .orders.callers_controller import CallersController
from .orders.calls_contoller import CallsController
from .orders.cities_controller import CitiesController
from .orders.emergency_reason_controller import EmergencyReasonController
from .orders.injuries_controller import InjuriesController
from .orders.rescuer_call_controller import RescuerCallsController
from .orders.rescuer_controller import RescuersController
from .orders.vehicle_controller import VehiclesController

cities_controller = CitiesController()
callers_controller = CallersController()
emergency_reasons_controller = EmergencyReasonController()
call_vehicle_controller = CallVehiclesController()
vehicles_controller = VehiclesController()
rescuer_controller = RescuersController()
rescuer_call_controller = RescuerCallsController()
injuries_controller = InjuriesController()
calls_controller = CallsController()
