from splitwise.services.user_service_interface import UserServiceInterface
from splitwise.models.user import User

class UserService(UserServiceInterface):
    userDetails = {}
    def addUser(self, id, name):
        user = User()
        user.setUserId(id)
        user.setUserName(name)
        self.__class__.userDetails[id]=user
        return user