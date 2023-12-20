class User:
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
    def change_password(self, old_password, new_password) -> None: # public
        self._is_password_correct(old_password)
        self._is_password_valid(new_password)
        self._was_password_used(new_password)
        
    def _is_password_correct(self, old_password):  # protected
        pass
        
    def _is_password_valid(self, new_password):  # private
        pass
    
    def _was_password_used(self, new_password):
        pass
    
    
    
user = User("John", '123123')

