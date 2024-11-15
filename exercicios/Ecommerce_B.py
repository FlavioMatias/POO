class Cliente:
    auto_id = 0 
    def __init__(self, name : str, email : str, telephone: int):
        Cliente.auto_id +=1
        self.__id = Cliente.auto_id
        self.__name = None
        self.__email = None
        self.__telephone = None

        self.set_name(name)
        self.set_email(email)
        self.set_telephone(telephone)

    def __str__(self):
        return rf""" 
────────────────────────────────────────────────────────────────
cliente: {self.__name}
email: {self.__email}
telefone: {self.__telephone}
────────────────────────────────────────────────────────────────
                 """
    
    def set_name(self, name) -> None:
        if name != None and isinstance(name, str):
            self.__name = name

        else: raise ValueError('nome invalido!')
        
    def set_email(self, email):
        if email != None and isinstance(email, str):
            self.__email = email

        else: raise ValueError('email invalido!')

    def set_telephone(self, number):
        if number != None and isinstance(number, int):
            self.__telephone = number
        
        else: raise ValueError('numero invalido')

    @property
    def get_telephone(self) -> int: return self.__telephone

    @property
    def get_id(self) -> int: return self.__id

    @property
    def get_email(self) -> str: return self.__email

    @property
    def get_name(self) -> str: return self.__name

    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "email": self.__email,
            "telephone": self.__telephone
        }

    @staticmethod
    def from_dict(data): return Cliente(name=data["name"], email=data["email"], telephone=data["telephone"])

    
    
class venda:pass

class vendaitem:pass

class produto:pass

class categoria:pass