from model.Produto import Produto
from controller.IControleDeEstoque import IControleDeEstoque


class ControleDeEstoque(IControleDeEstoque): 

    # instancia arrayList produtos com a classe dos objetos sendo Produto.
    def __init__(self):
        self.produtos = []

    def adicionarProduto(self, nome, quantidade):
        produto = Produto(nome, quantidade)  # instancia produto
        self.produtos.append(produto)
        # instancia um novo objeto na arraylist

    def getProdutos(self):
        return self.produtos
        # metodo get para pegar o valor do produto na arrayList

    def estoqueVazio(self):
        return len(self.produtos) == 0
        # metodo que verifica se o estoque esta vazio

    def buscarProduto(self, nome):
        for produto in self.produtos:
            if produto.getNome().lower() == nome.lower():
                return produto
        return None
        # verifica se existe o produto com base no nome dele.

    def retirarProduto(self, nome, quantidade):
        produto = self.buscarProduto(nome)
        if produto is None or quantidade > produto.getQuantidade():
            return False
        novaQuantidade = produto.getQuantidade() - quantidade
        produto.setQuantidade(novaQuantidade)

        return True
        # verifica se o produto existe, pega o produto pelo nome e retira a quantidade desejada.

    def alterarEstoque(self, nome, novoNome, novaQuantidade):
        produto = self.buscarProduto(nome)
        if produto is None:
            return False
        produto.setNome(novoNome)
        produto.setQuantidade(novaQuantidade)
        return True

        # metodo alterarEstoque, invoca buscarProduto, verifica se existe, se sim seta um novo nome
        # e uma nova quantidade

    def deletarProduto(self, nome):
        produto = self.buscarProduto(nome)
        if produto is None:
            return False
        self.produtos.remove(produto)
        return True
        # procura o produto no metodo buscarProduto, se achar o remove do estoque.