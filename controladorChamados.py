from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        self.__chamados = []
        self.__tipos_chamados = []

    @property
    def tipos_chamados(self) -> list:
        return self.__tipos_chamados

    @tipos_chamados.setter
    def tipos_chamado(self, tipos_chamados: list):
        if isinstance(tipos_chamados, list[TipoChamado]):
            self.__tipos_chamados = tipos_chamados

    @property
    def chamados(self) -> list:
        return self.__chamados

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        if not isinstance(tipo, TipoChamado):
            return 0
        contador_tipos_chamados = 0
        for chamado in self.chamados:
            if chamado.tipo is not None:
                if (
                    chamado.tipo.codigo == tipo.codigo
                    and chamado.tipo.codigo is not None
                ):
                    contador_tipos_chamados += 1
        return contador_tipos_chamados

    def inclui_chamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado
    ) -> Chamado:
        if self.__chamado_satisfaz_tipos(
            data,
            cliente,
            tecnico,
            titulo,
            descricao,
            prioridade,
            tipo
        ) and self.__verifica_chamado_nao_existe(
            data,
            cliente,
            tecnico,
            tipo
        ):
            chamado = Chamado(
                data,
                cliente,
                tecnico,
                titulo,
                descricao,
                prioridade,
                tipo
            )
            self.chamados.append(chamado)
            return chamado

    def inclui_tipochamado(
            self,
            codigo: int,
            nome: str,
            descricao: str) -> TipoChamado:
        if self.__verifica_tipo_chamado_nao_existe(codigo):
            tipo_chamado = TipoChamado(codigo, descricao, nome)
            self.tipos_chamado.append(tipo_chamado)
            return tipo_chamado

    def __verifica_chamado_nao_existe(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        tipo: TipoChamado
    ) -> bool:
        for chamado in self.chamados:
            if (
                chamado.data == data
                and chamado.cliente.codigo == cliente.codigo
                and chamado.tecnico.codigo == tecnico.codigo
                and chamado.tipo == tipo
            ):
                return False
        return True

    def __verifica_tipo_chamado_nao_existe(self, codigo: int) -> bool:
        for chamado in self.tipos_chamados:
            if chamado.codigo == codigo:
                return False
        return True

    def __chamado_satisfaz_tipos(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):
        if (
            isinstance(data, Date)
            and isinstance(cliente, Cliente)
            and isinstance(tecnico, Tecnico)
            and isinstance(titulo, str)
            and isinstance(descricao, str)
            and isinstance(prioridade, int)
            and isinstance(tipo, TipoChamado)
        ):
            return True
        return False
