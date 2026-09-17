from model.Produto import Produto
from controller.ControleDeEstoque import ControleDeEstoque


class MenuEstoque:
    controller = ControleDeEstoque()

    @staticmethod
    def iniciarInterface():
        opcao = -1

        while opcao != 0:
            MenuEstoque.mostrarMenu()

            try:
                opcao = int(input())
            except ValueError:
                print("Digite um número válido.")
                opcao = -1
                continue

            match opcao:
                case 1:
                    MenuEstoque.adicionarProdutos()
                case 2:
                    MenuEstoque.verEstoque()
                case 3:
                    MenuEstoque.alterarEstoque()
                    MenuEstoque.alterarOutroItem()
                case 4:
                    MenuEstoque.retirarProduto()
                case 5:
                    MenuEstoque.deletarProduto()
                case 0:
                    print("Programa encerrado.")
                case _:
                    print("Opção inválida, insira outra")
        # mostrar menu, requerir a escolha do funcionario e utilizar a funcionalidade desejada por ele enquanto for !0.

    @staticmethod
    def mostrarMenu():
        print("\n ============ CONTROLE DE ESTOQUE =============")
        print("ESCOLHA A FUNCIONALIDADE QUE DESEJA ACESSAR:")
        print("1 - ADICIONAR ITEM" + "\n2 - VER ESTOQUE" +"\n3 - ALTERAR ITEM DO ESTOQUE" +"\n4 - RETIRAR ITEM" +"\n5 - DELETAR ITEM"+ "0 - SAIR DO PROGRAMA\n")
  
        # interface para o usuario

    @staticmethod
    def alterarOutroItem():
        if not MenuEstoque.controller.estoqueVazio():
            print("Você deseja alterar outro item?")
            continuar = input()
        

            while continuar.lower() == "sim":
                MenuEstoque.alterarEstoque()

                print("Você deseja alterar outro item? (sim/não)")
                continuar = input()
#Metodo alterar para permitir que o usuario continue com o alterarEstoque
    @staticmethod
    def adicionarProdutos():
        print("Nome do item: ")
        nome = input()

        if not all(c.isalpha() or c.isspace() for c in nome):
            # maneira que encontrei de evitar que sejam usados numeros e simbolos
            print("\nDigite um nome válido.")
            return

        print("Quantidade do item: ")
        try:
            quantidade = int(input())
        except ValueError:
            print("Quantidade inválida.")
            return

        MenuEstoque.controller.adicionarProduto(nome, quantidade)
        print("Produto adicionado ao estoque")
        # interação ao usuario que manda a requisição para o controller, o qual aciona o metodo adicionarProduto

    @staticmethod
    def verEstoque():
        if MenuEstoque.controller.estoqueVazio():
            print("O Estoque está vazio")
            return
        # invoca estoqueVazio() para conferir se está vazio ou nao

        produtos = MenuEstoque.controller.getProdutos()
        # pega o conteudo da arraylist do controller

        for p in produtos:
            print(f"\nESTOQUE:\n \n{p.getNome()} - {p.getQuantidade()}")
        # para cada elemento dentro da arrayList, retorne nome e quantidade

    @staticmethod
    def alterarEstoque():
        if MenuEstoque.controller.estoqueVazio() == True:
            print("O Estoque está vazio")
            return
            # invoca estoqueVazio

        MenuEstoque.verEstoque()

        print("Nome do item que deseja alterar: ")
        nome = input()

        print("Novo nome do item: ")
        novoNome = input()

        print("Nova quantidade do item: ")
        try:
            novaQuantidade = int(input())
        except ValueError:
            print("Quantidade inválida.")
            return
        # invoca verEstoque, e pergunta as alterações ao usuário.

        existeProduto = MenuEstoque.controller.alterarEstoque(
            nome,
            novoNome,
            novaQuantidade
        )
        # invoca alterarProduto do controller para alterar os atributps

        if existeProduto:
            print("Produto alterado com sucesso")
        else:
            print("Produto não encontrado")
        # verifica se o produto é válido

    @staticmethod
    def retirarProduto():
        if MenuEstoque.controller.estoqueVazio() == True:
            print("O Estoque está vazio")
            return

        MenuEstoque.verEstoque()

        print("Nome do item que deseja retirar: ")
        nome = input()

        print("Quantidade que deseja retirar: ")
        try:
            quantidade = int(input())
        except ValueError:
            print("Quantidade inválida.")
            return

        existeProduto = MenuEstoque.controller.retirarProduto(nome, quantidade)
        # pergunta pro usuário oq e quantos ele quer retirar, após isso invoca retirarProduto.

        if existeProduto:
            print("Quantidade retirada com sucesso")
        else:
            print("Produto não encontrado ou quantidade insuficiente..")
        # condição para que seja retirada a quantidade do produto

    @staticmethod
    def deletarProduto():
        if MenuEstoque.controller.estoqueVazio() == True:
            print("O Estoque está vazio")
            return  # verifica se estoque esta vazio

        MenuEstoque.verEstoque()

        print("Nome do item que deseja deletar: ")
        nome = input()

        existeProduto = MenuEstoque.controller.deletarProduto(nome)
        # mostra o estoque e pede para usuario informar o nome do produto depois invoca o metodo deletarProduto
        # com parametro nome para retirar com base no "valor" digitado.

        if existeProduto:
            print("Produto deletado com sucesso")
        else:
            print("Produto não encontrado")
        # se o produto existe, ele pode ser deletado.