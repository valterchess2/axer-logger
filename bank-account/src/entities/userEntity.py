from utils.properties.cpf import CPF


class UserEntity:
    def __init__(self):
        self.name: str
        self.cpf: CPF()
