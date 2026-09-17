from abc import ABC, abstractmethod


class IControleDeEstoque(ABC):
    @abstractmethod
    def adicionarProduto(self, nome, quantidade):
        pass

    @abstractmethod
    def getProdutos(self):
        pass

    @abstractmethod
    def estoqueVazio(self):
        pass

    @abstractmethod
    def buscarProduto(self, nome):
        pass

    @abstractmethod
    def retirarProduto(self, nome, quantidade):
        pass

    @abstractmethod
    def alterarEstoque(self, nome, novoNome, novaQuantidade):
        pass

    @abstractmethod
    def deletarProduto(self, nome):
        pass

    #interface (contrato) qualquer classe que implementa-la deve ter alguns metodos obrigatórios