# Controle de Estoque — Python

## 1. Visão geral

O **Controle de Estoque** é uma aplicação desenvolvida em **Python** para gerenciamento básico de produtos. O sistema permite cadastrar produtos, consultar o estoque, alterar informações, retirar quantidades e excluir produtos.

A aplicação possui **duas interfaces**:

- **Interface via terminal** (`MenuEstoque.py`) — aplicação principal, totalmente funcional;
- **Dashboard web** (`dashboard.html`) — interface visual moderna **para fins de demonstração**, porém já funcional em seu estado atual.

O projeto utiliza uma arquitetura baseada em **MVC (Model-View-Controller)** com uma camada adicional de abstração: uma **interface de contrato** (`IEstoque`) implementada por meio de **ABC (Abstract Base Class)**, equivalente ao `interface` do Java.

---

## 2. Requisitos

### Software

- **Python 3.10 ou superior** (obrigatório por causa do `match/case` utilizado no menu)
- Navegador moderno (para visualizar o dashboard, opcional)
- Flask e Flask-CORS (opcionais, apenas para integração via API REST)

### Hardware

Não há requisitos específicos de hardware. O sistema possui baixo consumo de recursos e pode ser executado em computadores convencionais.

---

## 3. Estrutura do projeto

```text
ControleDeEstoque_python/
└── src/
    ├── Main.py
    ├── app.py
    │
    ├── model/
    │   ├── __init__.py
    │   └── Produto.py
    │
    ├── controller/
    │   ├── __init__.py
    │   ├── IEstoque.py
    │   └── ControleDeEstoque.py
    │
    ├── view/
    │   ├── __init__.py
    │   ├── MenuEstoque.py
    │   └── DashboardEstoque.py
    │
    └── static/
        └── dashboard.html


Controller
Responsável pelas operações e regras relacionadas ao estoque.

IEstoque.py

Define o contrato (interface) que qualquer implementação de controle de estoque deve seguir. Utiliza ABC e @abstractmethod. Métodos obrigatórios:

Método	Descrição
adicionarProduto(nome, quantidade, preco, categoria)	Adiciona um novo produto
getProdutos()	Retorna a lista de produtos
estoqueVazio()	Verifica se o estoque está vazio
buscarProduto(nome)	Busca produto pelo nome
retirarProduto(nome, quantidade)	Retira quantidade do estoque
alterarEstoque(nome, novoNome, novaQuantidade)	Altera dados do produto
deletarProduto(nome)	Remove produto do estoque
ControleDeEstoque.py

Implementa a interface IEstoque. Gerencia a lista de produtos e executa as operações de inclusão, busca, alteração, retirada e exclusão.

Model
Produto.py

Representa um produto armazenado no sistema.

Possui os seguintes atributos:

Atributo	Tipo	Descrição
nome	str	Nome do produto
quantidade	int	Quantidade disponível
preco	float	Preço unitário (opcional)
categoria	str	Categoria do produto
View
Responsável pela interação com o usuário.

MenuEstoque.py

Interface via terminal. Exibe o menu, recebe os dados digitados, realiza validações de entrada e solicita ao Controller a execução das operações. Utiliza match/case para o roteamento das opções do menu.

DashboardEstoque.py

Interface gráfica via CustomTkinter, com o mesmo design visual do dashboard web. Serve como alternativa nativa para ambientes desktop.

Main.py

Ponto de entrada da aplicação. Responsável por iniciar a interface do sistema.

4. Funcionalidades
Adicionar item
Cadastra um novo produto no estoque informando seu nome, quantidade, preço e categoria.

O nome do produto passa por uma validação para impedir o uso de números e símbolos, permitindo apenas letras e espaços.

Método: adicionarProdutos()

Ver estoque
Exibe todos os produtos cadastrados e suas respectivas quantidades.

Caso não existam produtos cadastrados, o sistema informa que o estoque está vazio.

Métodos utilizados:

estoqueVazio()

getProdutos()

Alterar item
Permite alterar o nome e a quantidade de um produto existente.

Método: alterarEstoque(nome, novoNome, novaQuantidade)

O sistema procura o produto pelo nome informado e, caso ele exista, atualiza seus dados.

Após realizar uma alteração, o sistema permite que o usuário escolha se deseja alterar outro item, podendo repetir a operação enquanto responder sim.

Retirar item
Reduz a quantidade disponível de um produto.

Método: retirarProduto(nome, quantidade)

A operação não é realizada caso o produto não exista ou a quantidade solicitada seja superior à quantidade disponível.

Deletar item
Remove completamente um produto do estoque.

Método: deletarProduto(nome)

5. Interface do sistema
5.1 Interface via terminal
Ao iniciar a aplicação, é apresentado o seguinte menu:

text
============ CONTROLE DE ESTOQUE =============
ESCOLHA A FUNCIONALIDADE QUE DESEJA ACESSAR:
1 - ADICIONAR ITEM
2 - VER ESTOQUE
3 - ALTERAR ITEM DO ESTOQUE
4 - RETIRAR ITEM
5 - DELETAR ITEM
0 - SAIR DO PROGRAMA
O usuário seleciona uma opção digitando o número correspondente.

Na opção de alteração, após modificar um produto, o sistema pergunta se o usuário deseja alterar outro item.

5.2 Dashboard web (demonstração)
⚠️ Observação: O arquivo dashboard.html é destinado exclusivamente à demonstração visual do projeto. Ele não substitui a aplicação principal em Python, servindo como protótipo de interface moderna para apresentação.

Entretanto, o dashboard já se encontra funcional: todos os botões (Adicionar, Alterar, Retirar, Buscar, Deletar) executam ações reais no estado local, atualizam a lista de produtos, o log de operações e as métricas em tempo real.

Para abrir o dashboard, basta executar:

bash
start static/dashboard.html      # Windows
open static/dashboard.html       # macOS
xdg-open static/dashboard.html   # Linux
Características do dashboard:

Tema dark mode com acento verde-menta único

Tipografia editorial (Playfair Display para títulos, JetBrains Mono para dados)

Layout em grid com hierarquia clara (header → métricas → ações → lista → log)

Cinco botões funcionais que abrem modais para execução de cada operação

Log de operações em tempo real

Métricas agregadas (total de itens, valor em estoque, itens em atenção)

6. Fluxo da aplicação
A aplicação segue o fluxo:

text
Usuário
   ↓
MenuEstoque / DashboardEstoque
   ↓
ControleDeEstoque  ──── implementa ──▶  IEstoque (ABC)
   ↓
Produto
A View recebe a entrada do usuário e encaminha a solicitação para o Controller. O Controller executa a operação sobre os objetos Produto armazenados na lista.

7. Armazenamento dos dados
Os produtos são armazenados em memória utilizando uma lista Python:

python
self.produtos = []
Os dados permanecem disponíveis enquanto o programa estiver em execução.

Observação: a versão atual não utiliza banco de dados ou armazenamento permanente. Ao encerrar o programa, os produtos cadastrados são perdidos.

8. Interface e arquitetura
O projeto utiliza MVC com uma camada adicional de contrato:

Model: representa os dados (Produto);

View: interação com o usuário (MenuEstoque, DashboardEstoque e Main);

Controller: gerenciamento e regras do estoque (ControleDeEstoque);

Interface: contrato de métodos obrigatórios (IEstoque).

A MenuEstoque utiliza uma instância de ControleDeEstoque para encaminhar as operações realizadas pelo usuário, mantendo a separação entre a interface e o gerenciamento dos dados.

Interface de contrato (ABC)
Em Python, a interface é definida da seguinte forma:

python
from abc import ABC, abstractmethod

class IEstoque(ABC):
    @abstractmethod
    def adicionarProduto(self, nome, quantidade):
        pass
    # ...
E implementada por:

python
class ControleDeEstoque(IEstoque):
    def adicionarProduto(self, nome, quantidade):
        # ...
Essa construção é equivalente ao par interface / implements do Java.

9. Execução
Versão terminal
Abra o terminal no diretório src/.

Execute:

bash
python Main.py
Utilize o menu exibido no terminal para realizar as operações.

Versão com API REST (opcional)
Instale as dependências:

bash
pip install flask flask-cors
Execute:

bash
python app.py
Acesse http://localhost:5000 no navegador.

Endpoints da API
Método	Rota	Descrição
GET	/api/produtos	Lista todos os produtos
POST	/api/produtos	Adiciona novo produto
GET	/api/produtos/<nome>	Busca produto por nome
PUT	/api/produtos/<nome>	Altera produto
POST	/api/produtos/<nome>/retirar	Retira quantidade
DELETE	/api/produtos/<nome>	Remove produto
GET	/api/metricas	Retorna métricas agregadas
10. Tratamento das operações
O sistema utiliza valores booleanos para informar o resultado de algumas operações.

Por exemplo:

python
sucesso = controller.retirarProduto(nome, quantidade)
O retorno True indica que a operação foi realizada. O retorno False indica que a operação não pôde ser realizada, como no caso de um produto inexistente ou quantidade insuficiente.

O sistema também verifica se o estoque está vazio antes de executar operações que dependem da existência de produtos.

Tratamento de exceções
Entradas numéricas são tratadas com try/except ValueError, evitando que o programa seja encerrado por digitação incorreta.

11. Limitações atuais
Os dados são armazenados somente em memória.

Não há persistência em banco de dados.

Não existe autenticação de usuários.

A interface principal é executada exclusivamente pelo terminal.

O dashboard web é uma demonstração e não está conectado ao back-end Python por padrão.

A validação de entrada é limitada aos campos atualmente tratados pela interface.

12. Possíveis evoluções
O sistema pode ser posteriormente expandido para incluir:

Persistência em banco de dados (SQLite, PostgreSQL);

Integração completa entre dashboard web e back-end Flask;

Cadastro de usuários e níveis de acesso;

Controle de fornecedores;

Histórico de movimentações com data e hora;

Relatórios de estoque (CSV, PDF);

Alertas automáticos de estoque mínimo;

Testes automatizados com pytest.

13. Comparativo Java × Python
O projeto foi originalmente concebido em Java e posteriormente portado para Python. As principais adaptações foram:

Java	Python
interface IEstoque	class IEstoque(ABC)
implements IEstoque	class ControleDeEstoque(IEstoque)
@Override	(opcional, apenas documentação)
ArrayList<Produto>	list
switch/case	match/case (Python 3.10+)
Scanner	input()
Getters/Setters explícitos	Atributos diretos ou @property
System.out.println()	print()
Thread.sleep(1000)	time.sleep(1)
text

---

## 📄 `model/__init__.py`

```python
(arquivo vazio)

📄 model/Produto.py
python
class Produto:

    def __init__(self, nome, quantidade, preco=0.0, categoria="Geral"):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria
        # define o escopo (classe) dos obj

    def getNome(self):
        return self.nome

    def getQuantidade(self):
        return self.quantidade

    def setNome(self, nome):
        self.nome = nome

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
        # getters e setters

    def to_dict(self):
        """Converte o produto em dicionário — usado pela API REST."""
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "categoria": self.categoria,
            "sku": str(hash(self.nome) % 10000).zfill(4),
        }
📄 controller/__init__.py
python
(arquivo vazio)

📄 controller/IEstoque.py
python
from abc import ABC, abstractmethod


class IEstoque(ABC):
    """
    Interface (contrato) que define os métodos obrigatórios
    para qualquer implementação de controle de estoque.
    Equivale ao 'public interface IEstoque' do Java.
    """

    @abstractmethod
    def adicionarProduto(self, nome, quantidade, preco=0.0, categoria="Geral"):
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
📄 controller/ControleDeEstoque.py
python
from model.Produto import Produto
from controller.IEstoque import IEstoque


class ControleDeEstoque(IEstoque):  # equivale a "implements IEstoque"

    # instancia arrayList produtos com a classe dos objetos sendo Produto.
    def __init__(self):
        self.produtos = []
        # construtor

    def adicionarProduto(self, nome, quantidade, preco=0.0, categoria="Geral"):
        if self.buscarProduto(nome):
            return False
        produto = Produto(nome, quantidade, preco, categoria)  # instancia produto
        self.produtos.append(produto)
        # instancia um novo objeto na arraylist
        return True

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
📄 view/__init__.py
python
(arquivo vazio)

📄 view/MenuEstoque.py
python
