database = open("userData", "r")
        
database.close()

class User:
    def __init__(self, password, email):
        self.password = password
        self.email = email