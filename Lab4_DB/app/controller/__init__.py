from .clients_controller import ClientController
from .animators_controller import AnimatorController
from .order_animators_controller import OrderAnimatorController
from .orders_controller import OrderController
from .agencies_controller import AgencyController
from .animator_orders_controller import AnimatorOrderController
from .employees_controller import EmployeeController
from .event_types_controller import EventTypeController

client_controller = ClientController()
animator_controller = AnimatorController()
order_animator_controller = OrderAnimatorController()
order_controller = OrderController()
agency_controller = AgencyController()
animator_order_controller = AnimatorOrderController()
employee_controller = EmployeeController()
event_type_controller = EventTypeController()
