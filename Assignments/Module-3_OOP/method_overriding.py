class master:
    def signin(self,username,password): #original
        print("Username:",username)
        print("Password:",password)

class home(master):
    def signin(self, username, password): #xerox
        return super().signin(username, password)

class about(master):
    def signin(self, username, password):
        return super().signin(username, password)