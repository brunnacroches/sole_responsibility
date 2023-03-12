class RegistrationSystem:
    
    def register(self, name:str, age:int) -> None:
        if self.__verify_data(name, age):
            self.__store_user(name, age)
        else:
            self.__indicate_error()
    
    def __verify_data(self, name:str, age:int) -> None:
        if isinstance(name, str) and isinstance(age, int):
            return True
        else:
            return False
    
    def __store_user(self, name:str, age: int) -> None:
        print('Accessing the database...')
        print('Register User {}, age{}'.format(name, age))
    
    def __indicate_error(self) -> None:
        print('dados inválidos')
        
## test
## on terminal :
## python3
## >>> from registration_system import RegistrationSystem
## >>> sis = RegistrationSystem()
## >>> sis.register('Brunna', 28)