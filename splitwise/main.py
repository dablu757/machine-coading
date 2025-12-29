from splitwise.factory.controller_factory import ControllerFactory

userController = ControllerFactory.create_user_controller()
groupController = ControllerFactory.create_group_controller()
billController = ControllerFactory.create_bill_controller()

user1 = userController.addUser("user1", "abhi")
user2 = userController.addUser("user2", "chainsi")
user3 = userController.addUser("user3", "ranjeet")
user4 = userController.addUser("user4", "satish")
user5 = userController.addUser("user5", "dablu")

members = [user1, user2, user3, user4, user5]

group1 = groupController.addGroup("group1", "avenger", members)

contribution = {
    'user1': 100,
    'user2': 100,
    'user3': 100,
    'user4': 100,
    'user5': 100
}

paidBy = {
    'user1': 200,
    'user2': 50,
    'user3': 50,
    'user4': 100,
    'user5': 100
}

billController.addBill("bill1", "group1", 500, contribution, paidBy)

balance = billController.getUserBalance("user2")
print(balance)














# from splitwise.controllers.bill_controller import BillController
# from splitwise.controllers.user_controller import UserController
# from splitwise.controllers.group_controller import GroupController

# from splitwise.services.bill_service import BillService
# from splitwise.services.user_service import UserService
# from splitwise.services.group_service import GroupService

# userController = UserController(UserService())
# groupController = GroupController(GroupService())
# billController = BillController(BillService())

# user1 = userController.addUser("user1","abhi")
# user2 = userController.addUser("user2","chainsi")
# user3 = userController.addUser("user3","ranjeet")
# user4 = userController.addUser("user4","satish")
# user5 = userController.addUser("user5","dablu")

# members = [user1,user2,user3,user4,user5]

# group1 = groupController.addGroup('group1','avenger',members)
# # print(group1.getMembers())

# contribution = {'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}
# paidBy = {'user1':200,'user2':50,'user3':50,'user4':100,'user5':100}
# bill = billController.addBill('bill1','group1',500,contribution,paidBy)
# balance = billController.getUserBalance('user2')
# print(balance)