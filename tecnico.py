from pessoa import Pessoa


class Tecnico(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)

    @property
    def nome(self) -> str:
        return super().nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            super().nome = nome

    @property
    def codigo(self) -> int:
        return super().codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            super().codigo = codigo
