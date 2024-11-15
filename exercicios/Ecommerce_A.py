class Cliente:
    def __init__(self, name : str, email : str, telephone: int):
        self.__id = id(self)
        self.__name = None
        self.__email = None
        self.__telephone = None

        self.set_name(name)
        self.set_email(email)
        self.set_telephone(telephone)

    def __str__(self):
        return rf""" 
cliente: {self.__name}
email: {self.__email}
telefone: {self.__telephone}
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

    
class Clientes:
    """ lista que armazena clientes"""
    __objects : list = [] 

    @classmethod
    def insert(cls, cliente : object):
        cls.__objects.append(cliente)

    @classmethod
    def list(cls):
        if len(cls.__objects) == 0: raise ValueError('nao existe nenhum cliente')

        else:
            client_name = []
            for clientes in cls.__objects:
                client_name.append((clientes.get_id,clientes.get_name))

            return client_name
        
    @classmethod
    def list_id(cls, Id_de_busca : int) -> object:
        for client in cls.__objects:
            if client.get_id == Id_de_busca:
                return client
            
        raise ValueError('cliente não encontrado')
    
    @classmethod
    def update(cls, cliente : object):
        cliente.set_name(input('insira o novo nome: '))
        cliente.set_email(input('insira o novo email: '))
        cliente.set_telephone(input('insira o novo telefone: '))

    @classmethod
    def delete(cls, cliente : object):
        cls.__objects.remove(cliente)

    @classmethod
    def save(cls, file_path: str = 'json/clients.json'):
        """Salva os clientes no arquivo JSON"""

        import json
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([cliente.to_dict() for cliente in cls.__objects], f, ensure_ascii=False, indent=4)

    @classmethod
    def load(cls, file_path: str = 'json/clients.json'):
        """Carrega os clientes de um arquivo JSON"""

        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            cls.__objects = [Cliente.from_dict(item) for item in data]

class UI:

    @classmethod
    def main(cls):
        Clientes.load()
        op = cls.__menu()

        while True:

            match op:

                case 1:
                    cls.__listar()

                case 2:
                    cls.__inserir()

                case 3:
                    cls.__atualizar()

                case 4:
                    cls.__excluir()

                case 0:
                    print("ate a proxima")
                    Clientes.save()
                    break
            op = cls.__menu()
            Clientes.save()
    
    @staticmethod
    def __menu():
        print(r'''
escolha uma das operações a baixo

[1]listar      [3]atualizar     [0]sair
[2]inserir     [4]excluir       
              ''')
        return int(input('> '))
    
    @staticmethod
    def __inserir():
        Clientes.insert(Cliente(
            name= input("digite seu nome: "),
            email= input("digite seu email: "),
            telephone= int(input("digite seu telefone: "))
            ))
        
    def __listar():
        for clientes in Clientes.list():
            print(f"{clientes[0]} : {clientes[1]}")

"""pojo e dao class"""


if __name__ == "__main__":
    UI.main()