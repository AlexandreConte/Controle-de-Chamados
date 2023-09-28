from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        if isinstance(codigo, int) and isinstance(nome, str):
            for cliente in self.clientes:
                if codigo == cliente.codigo:
                    break
            else:
                cliente = Cliente(nome, codigo)
                self.clientes.append(cliente)
                return cliente

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        if isinstance(codigo, int) and isinstance(nome, str):
            for tecnico in self.tecnicos:
                if tecnico.codigo == codigo:
                    break
            else:
                tecnico = Tecnico(nome, codigo)
                self.tecnicos.append(tecnico)
                return tecnico
