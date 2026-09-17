# 📦 Controle de Estoque — Python

Sistema de controle de estoque desenvolvido em **Python** com arquitetura **MVC** (Model-View-Controller) e **interface de contrato** (`ABC`). Inclui versão console funcional, dashboard web de demonstração e API REST opcional.

---

## 📋 Índice

- [Visão geral](#-visão-geral)
- [Requisitos](#-requisitos)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Arquitetura](#-arquitetura)
- [Funcionalidades](#-funcionalidades)
- [Como executar](#-como-executar)
- [Dashboard web](#-dashboard-web)
- [API REST](#-api-rest)
- [Tratamento de operações](#-tratamento-de-operações)
- [Limitações atuais](#-limitações-atuais)
- [Possíveis evoluções](#-possíveis-evoluções)
- [Comparativo Java × Python](#-comparativo-java--python)
- [Tecnologias](#-tecnologias)

---

## 🎯 Visão geral

O **Controle de Estoque** é uma aplicação para gerenciamento básico de produtos. O sistema permite:

- Cadastrar produtos (nome, quantidade, preço e categoria)
- Consultar o estoque completo
- Buscar produtos pelo nome
- Alterar dados de produtos existentes
- Retirar quantidades do estoque
- Excluir produtos

A aplicação possui **três interfaces**:

| Interface | Arquivo | Descrição |
|-----------|---------|-----------|
| **Terminal** | `MenuEstoque.py` | Aplicação principal, totalmente funcional |
| **Dashboard web** | `static/dashboard.html` | Interface visual moderna — **demonstração**, porém funcional |
| **Desktop nativo** | `DashboardEstoque.py` | Alternativa em `CustomTkinter` (opcional) |

O projeto utiliza **MVC** com uma camada adicional de abstração: uma **interface de contrato** (`IEstoque`) implementada via **ABC (Abstract Base Class)**, equivalente ao `interface` do Java.

---

## ⚙️ Requisitos

### Software

- **Python 3.10 ou superior** (obrigatório por causa do `match/case` no menu)
- Navegador moderno (para o dashboard web, opcional)
- Flask e Flask-CORS (opcionais, apenas para a API REST)
- CustomTkinter (opcional, apenas para a versão desktop)

### Hardware

Não há requisitos específicos. O sistema possui baixo consumo de recursos e roda em computadores convencionais.

---

## 📁 Estrutura do projeto

```text
ControleDeEstoque_python/
└── src/
    ├── Main.py                        # Entrada da versão console
    ├── app.py                         # Servidor Flask (opcional)
    │
    ├── model/
    │   ├── __init__.py
    │   └── Produto.py                 # Entidade Produto
    │
    ├── controller/
    │   ├── __init__.py
    │   ├── IEstoque.py                # Interface (contrato ABC)
    │   └── ControleDeEstoque.py       # Implementação do contrato
    │
    ├── view/
    │   ├── __init__.py
    │   ├── MenuEstoque.py             # Menu console
    │   └── DashboardEstoque.py        # Dashboard desktop (opcional)
    │
    └── static/
        └── dashboard.html             # Dashboard web (demonstração)
