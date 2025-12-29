class User(object):
    def __init__(self):
        self.userId = None
        self.userName = None

    def setUserId(self,userId):
        self.userId = userId
    
    def getUserId(self):
        return self.userId
    
    def setUserName(self,userName):
        self.userName = userName

    def getUserName(self):
        return self.userName