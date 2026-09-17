📦 Controle de Estoque — Python

Sistema de controle de estoque desenvolvido em Python utilizando arquitetura MVC (Model-View-Controller) e interfaces de contrato com ABC (Abstract Base Class). O projeto oferece uma versão principal em terminal, uma interface desktop opcional e um dashboard web integrado a uma API REST desenvolvida com Flask.

📋 Índice
#-visão-geral
#️-requisitos
#-estrutura-do-projeto
#️-arquitetura
#-funcionalidades
#-como-executar
#-dashboard-web
#-api-rest
#-tratamento-de-operações
#️-limitações-atuais
#-possíveis-evoluções
#-comparativo-java--python
#️-tecnologias
🎯 Visão Geral

O Controle de Estoque é uma aplicação para gerenciamento de produtos que permite realizar operações comuns de estoque de forma simples e organizada.

Funcionalidades principais
Cadastro de produtos
Consulta do estoque completo
Busca de produtos por nome
Alteração de dados de produtos
Retirada de itens do estoque
Exclusão de produtos
Visualização de métricas do estoque
Integração com API REST
Interfaces disponíveis
Interface	Arquivo	DescriçãoTerminal	MenuEstoque.py	Aplicação principal totalmente funcional
Dashboard Web	static/dashboard.html	Interface visual moderna para demonstração e integração
Desktop	DashboardEstoque.py	Aplicação desktop usando CustomTkinter

O sistema segue o padrão MVC, utilizando uma camada adicional de abstração através da interface IEstoque, implementada com ABC (Abstract Base Class).

Hardware

Não existem requisitos específicos. O sistema possui baixo consumo de recursos e pode ser executado em qualquer computador moderno.

📁 Estrutura do Projeto
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

Observação

Os arquivos abaixo devem existir vazios para que os diretórios sejam reconhecidos como pacotes Python:

model/__init__.py
controller/__init__.py
view/__init__.py

🏗️ Arquitetura

O projeto segue o padrão MVC com uma camada extra de contrato baseada em interface.

Usuário
   ↓
MenuEstoque / DashboardEstoque / dashboard.html
   ↓
ControleDeEstoque ─── implementa ───▶ IEstoque (ABC)
   ↓
Produto

Camadas da aplicação
Camada	ResponsabilidadeModel	Representação dos dados
View	Interação com o usuário
Controller	Regras de negócio
Interface	Contrato obrigatório dos métodos
Arquivos por camada

Model

Produto.py

View

MenuEstoque.py
DashboardEstoque.py
dashboard.html

Controller

ControleDeEstoque.py

Interface

IEstoque.py
📜 Interface IEstoque

A interface IEstoque define o contrato obrigatório que qualquer implementação de controle de estoque deve seguir.

Métodos obrigatórios
Método	DescriçãoadicionarProduto()	Adiciona um novo produto
getProdutos()	Retorna todos os produtos
estoqueVazio()	Verifica se existem itens cadastrados
buscarProduto()	Busca um produto pelo nome
retirarProduto()	Remove quantidade do estoque
alterarEstoque()	Atualiza dados do produto
deletarProduto()	Remove produto do estoque
Exemplo da interface
from abc import ABC, abstractmethod

class IEstoque(ABC):

    @abstractmethod
    def adicionarProduto(self, nome, quantidade):
        pass

Implementação
class ControleDeEstoque(IEstoque):

    def adicionarProduto(self, nome, quantidade):
        pass


Essa abordagem é equivalente ao padrão interface + implements utilizado em Java.

✅ Funcionalidades
➕ Adicionar Produto

Permite cadastrar um produto informando:

Nome
Quantidade
Preço
Categoria

Validações:

Apenas letras e espaços são permitidos no nome.
Não permite entradas inválidas para quantidade ou preço.

Método utilizado

adicionarProduto()

📦 Visualizar Estoque

Exibe todos os produtos cadastrados.

Caso não existam produtos, o sistema informa que o estoque está vazio.

Métodos utilizados

estoqueVazio()
getProdutos()

✏️ Alterar Produto

Permite modificar:

Nome
Quantidade

Método

alterarEstoque(nome, novoNome, novaQuantidade)


Caso o produto exista, as alterações são realizadas imediatamente.

➖ Retirar Produto

Reduz a quantidade disponível de um produto.

Método

retirarProduto(nome, quantidade)


Validações:

Produto deve existir.
Quantidade solicitada não pode ser maior que a disponível.
🗑️ Deletar Produto

Remove completamente um produto do estoque.

Método

deletarProduto(nome)

🔎 Buscar Produto

Localiza um produto através do nome.

Método

buscarProduto(nome)

🚀 Como Executar
Versão Console (Principal)
cd ControleDeEstoque_python/src
python Main.py

Menu Principal
============ CONTROLE DE ESTOQUE =============

ESCOLHA A FUNCIONALIDADE QUE DESEJA ACESSAR:

1 - ADICIONAR ITEM
2 - VER ESTOQUE
3 - ALTERAR ITEM DO ESTOQUE
4 - RETIRAR ITEM
5 - DELETAR ITEM
0 - SAIR DO PROGRAMA

🎨 Dashboard Web

O dashboard web foi desenvolvido para fornecer uma visualização moderna do sistema.

Modo Demonstração
# Windows
start static/dashboard.html

# macOS
open static/dashboard.html

# Linux
xdg-open static/dashboard.html

Modo Integrado

Execute o servidor Flask:

python app.py


Depois acesse:

http://localhost:5000

Recursos do Dashboard
🌙 Tema Dark Mode
🎨 Destaque visual verde-menta
📊 Métricas de estoque em tempo real
📝 Log de operações
🔎 Busca de produtos
➕ Adição de produtos
✏️ Alteração de produtos
➖ Retirada de itens
🗑️ Exclusão de produtos
🔄 Atualização automática dos dados
Comportamento Inteligente

O dashboard identifica automaticamente o ambiente:

Executado pelo navegador → utiliza armazenamento local.
Executado via Flask → consome a API REST.
🔌 API REST
Executar API
pip install flask flask-cors

cd ControleDeEstoque_python/src

python app.py

Endpoints
Método	Rota	DescriçãoGET	/api/produtos	Lista produtos
POST	/api/produtos	Cria produto
GET	/api/produtos/<nome>	Busca produto
PUT	/api/produtos/<nome>	Atualiza produto
POST	/api/produtos/<nome>/retirar	Retira quantidade
DELETE	/api/produtos/<nome>	Exclui produto
GET	/api/metricas	Retorna métricas
Exemplos

Listar produtos:

curl http://localhost:5000/api/produtos


Adicionar produto:

curl -X POST http://localhost:5000/api/produtos \
-H "Content-Type: application/json" \
-d '{
    "nome":"Headset",
    "quantidade":10,
    "preco":249.90,
    "categoria":"Perifericos"
}'


Retirar produto:

curl -X POST http://localhost:5000/api/produtos/Headset/retirar \
-H "Content-Type: application/json" \
-d '{
    "quantidade":2
}'

🔄 Tratamento de Operações

As operações retornam valores booleanos indicando sucesso ou falha.

sucesso = controller.retirarProduto(nome, quantidade)

Retornos
True


Operação realizada com sucesso.

False


Operação falhou devido a:

Produto inexistente
Quantidade insuficiente
Operação inválida
Tratamento de Exceções

Entradas numéricas são protegidas com:

try:
    quantidade = int(input())
except ValueError:
    print("Valor inválido")


Isso evita encerramentos inesperados da aplicação.

⚠️ Limitações Atuais
Dados armazenados apenas em memória
Não utiliza banco de dados
Não possui autenticação
Sem controle de permissões
Interface principal baseada em terminal
Dashboard web voltado para demonstração
Validações básicas de entrada
🔮 Possíveis Evoluções
Persistência com SQLite
Persistência com PostgreSQL
Integração completa com Flask
Controle de usuários e perfis
Gestão de fornecedores
Histórico de movimentações
Exportação CSV
Exportação PDF
Alertas de estoque mínimo
Testes automatizados com Pytest
Dockerização da aplicação
Pipeline CI/CD
☕ Comparativo Java × Python
Conceito	Java	PythonInterface	interface	ABC
Implementação	implements	Herança
Método abstrato	abstract	@abstractmethod
Encapsulamento	Forte	Convencional
Verbosidade	Alta	Baixa
Curva de aprendizado	Média	Baixa

Exemplo Java:

public interface IEstoque {
    void adicionarProduto(String nome, int quantidade);
}


Equivalente em Python:

from abc import ABC, abstractmethod

class IEstoque(ABC):

    @abstractmethod
    def adicionarProduto(self, nome, quantidade):
        pass

🛠️ Tecnologias
Python 3.10+
MVC (Model-View-Controller)
ABC (Abstract Base Class)
Flask
Flask-CORS
CustomTkinter
HTML5
CSS3
JavaScript
REST API
JSON
👨‍💻 Autor
