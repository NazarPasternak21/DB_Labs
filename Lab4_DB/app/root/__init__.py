from flask import Flask

from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .employees_route import employee_bp
    from .animators_route import animator_bp
    from .order_animators_route import order_animator_bp
    from .event_types_route import event_type_bp
    from .agencies_route import agency_bp
    from .animator_orders_route import animator_order_bp
    from .clients_route import client_bp
    from .orders_route import order_bp

    app.register_blueprint(employee_bp)
    app.register_blueprint(animator_bp)
    app.register_blueprint(order_animator_bp)
    app.register_blueprint(event_type_bp)
    app.register_blueprint(agency_bp)
    app.register_blueprint(animator_order_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(order_bp)
