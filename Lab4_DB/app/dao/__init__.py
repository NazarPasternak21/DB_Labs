from .employees_dao import EmployeeDAO
from .event_types_dao import EventTypeDAO
from .animators_dao import AnimatorDAO
from .orders_dao import OrderDAO
from .agencies_dao import AgencyDAO
from .clients_dao import ClientDAO
from .order_animators_dao import OrderAnimatorDAO
from .animator_orders_dao import AnimatorOrderDAO

employees_dao = EmployeeDAO()
event_types_dao = EventTypeDAO()
animators_dao = AnimatorDAO()
orders_dao = OrderDAO()
agencies_dao = AgencyDAO()
clients_dao = ClientDAO()
order_animators_dao = OrderAnimatorDAO()
animator_orders_dao = AnimatorOrderDAO()
