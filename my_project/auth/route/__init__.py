from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)
    from .orders.call_vehicle_route import call_vehicles_bp
    from .orders.vehicle_route import vehicles_bp
    from .orders.callers_route import callers_bp
    from .orders.cities_route import cities_bp
    from .orders.rescuer_route import rescuers_bp
    from .orders.calls_route import calls_bp
    from .orders.rescuer_call_route import rescuer_calls_bp
    from .orders.injuries_route import injuries_bp
    from .orders.emergency_reasons_route import emergency_reasons_bp

    app.register_blueprint(emergency_reasons_bp)
    app.register_blueprint(injuries_bp)
    app.register_blueprint(rescuer_calls_bp)
    app.register_blueprint(calls_bp)
    app.register_blueprint(rescuers_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(callers_bp)
    app.register_blueprint(vehicles_bp)
    app.register_blueprint(call_vehicles_bp)
