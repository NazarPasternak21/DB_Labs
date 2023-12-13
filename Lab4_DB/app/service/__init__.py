from .clients_service import ClientService
from .animators_service import AnimatorService
from .order_animators_service import OrderAnimatorService
from .event_types_service import EventTypeService
from .agencies_service import AgenciesService
from .animator_orders_service import AnimatorOrderService
from .employees_service import EmployeeService
from .orders_service import OrderService

client_service = ClientService()
animator_service = AnimatorService()
order_animator_service = OrderAnimatorService()
event_type_service = EventTypeService()
agency_service = AgenciesService()
animator_order_service = AnimatorOrderService()
employee_service = EmployeeService()
order_service = OrderService()
