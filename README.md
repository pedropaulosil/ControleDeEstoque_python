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
