class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def test_func(self):
        print(self.username)
        
    # def hash_password():
    #     pass
