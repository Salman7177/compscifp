class UserObject(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def test_func(self):
        pass
    
    
    def hash_password(self):
        num = int(self.password)
        print(num)
        
        hashmap = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        
        hex_str = ''
        if num == 0:
            return "0"
        while num > 0:
            
            hex_val = num % 16
            num = num // 16
            
            if hex_val >= 10:
                hex_str = hashmap[hex_val] + hex_str
            else:
                hex_str = str(hex_val) + hex_str    
        print(hex_str)
        
