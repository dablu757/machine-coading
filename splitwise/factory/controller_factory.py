from splitwise.controllers.user_controller import UserController
from splitwise.controllers.group_controller import GroupController
from splitwise.controllers.bill_controller import BillController

from splitwise.services.user_service import UserService
from splitwise.services.group_service import GroupService
from splitwise.services.bill_service import BillService


class ControllerFactory:

    @staticmethod
    def create_user_controller():
        return UserController(UserService())

    @staticmethod
    def create_group_controller():
        return GroupController(GroupService())

    @staticmethod
    def create_bill_controller():
        return BillController(BillService())
