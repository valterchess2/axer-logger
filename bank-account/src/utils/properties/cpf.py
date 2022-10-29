class CPF:
    def __init__(self, cpf_str):
        self.cpf_str: str = cpf_str
        self.verify_cpf = VerifyCPF()

    @property
    def cpf(self):
        # verify if CPF is in correct format
        self.verify_cpf.is_valid()
