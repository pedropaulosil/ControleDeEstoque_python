# ControleDeEstoque_python

# 📦 Controle de Estoque — Sistema Operacional

Sistema de controle de estoque desenvolvido em **Python** com arquitetura **MVC** (Model-View-Controller) e **interface de contrato (ABC)**. Inclui uma versão console funcional e um **dashboard web** para demonstração visual do projeto.

---

## 📋 Índice

- [Sobre o projeto](#-sobre-o-projeto)
- [Arquitetura](#-arquitetura)
- [Estrutura de pastas](#-estrutura-de-pastas)
- [Como executar](#-como-executar)
- [Dashboard Web (demonstração)](#-dashboard-web-demonstração)
- [API REST (opcional)](#-api-rest-opcional)
- [Tecnologias](#-tecnologias)
- [Funcionalidades](#-funcionalidades)
- [Autor](#-autor)

---

## 🎯 Sobre o projeto

Este projeto implementa um **sistema de controle de estoque** com as seguintes características:

- **Arquitetura MVC** — separação clara entre Model, View e Controller
- **Interface de contrato** (`IEstoque`) usando **Abstract Base Class (ABC)** — equivalente ao `interface` do Java
- **CRUD completo** de produtos: adicionar, listar, buscar, alterar, retirar e deletar
- **Versão console** funcional via `MenuEstoque`
- **Dashboard web** moderno para demonstração visual (HTML/CSS/JS)

---

## 🏗️ Arquitetura

O projeto segue o padrão **MVC** com uma camada extra de abstração via **interface**:
