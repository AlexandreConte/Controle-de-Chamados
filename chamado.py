from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):
        self.__data = (None, data)[isinstance(data, Date)]
        self.__cliente = (None, cliente)[isinstance(cliente, Cliente)]
        self.__tecnico = (None, tecnico)[isinstance(tecnico, Tecnico)]
        self.__titulo = (None, titulo)[isinstance(titulo, str)]
        self.__descricao = (None, descricao)[isinstance(descricao, str)]
        self.__prioridade = (None, prioridade)[isinstance(prioridade, int)]
        self.__tipo = (None, tipo)[isinstance(tipo, TipoChamado)]

    @property
    def data(self) -> Date:
        return self.__data

    @data.setter
    def data(self, data: Date):
        if isinstance(data, Date):
            self.__data = data

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def tecnico(self) -> Tecnico:
        return self.__tecnico

    @tecnico.setter
    def tecnico(self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao

    @property
    def prioridade(self) -> int:
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade: int):
        if isinstance(prioridade, int):
            self.__prioridade = prioridade

    @property
    def tipo(self) -> TipoChamado:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoChamado):
        if isinstance(tipo, TipoChamado):
            self.__tipo = tipo
