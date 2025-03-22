# Aplicativo de Compras

Este é um aplicativo de compras desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e SQLite3 para o banco de dados. O sistema permite que os usuários realizem diversas operações, como cadastrar clientes, cadastrar produtos, adicionar produtos ao carrinho, finalizar compras e gerenciar produtos.

---

## Funcionalidades

- **Login e Cadastro de Usuários**: Os usuários podem fazer login no sistema ou se cadastrar fornecendo informações como nome, email, senha e outros dados necessários.
- **Cadastro de Produtos**: É possível cadastrar produtos com detalhes como nome, descrição, preço e quantidade em estoque.
- **Adicionar Produtos ao Carrinho**: Os usuários podem adicionar produtos ao carrinho de compras.
- **Finalizar Compra**: Os usuários podem finalizar a compra dos produtos adicionados ao carrinho.
- **Gerenciamento de Produtos**: Acesso a uma interface de gerenciamento onde é possível cadastrar, editar e remover produtos.

---

## Requisitos

- Python 3  
- Bibliotecas padrão do Python (Tkinter e SQLite3 já estão incluídas na instalação padrão do Python).

---

## Estrutura do Projeto

- **`app.py`**: Arquivo principal do sistema, responsável pela interface inicial.
- **`login.py`**: Interface para login de usuários.
- **`register.py`**: Interface para cadastro de novos usuários.
- **`registerProduct.py`**: Interface para cadastrar produtos.
- **`deleteProduct.py`**: Interface para remover produtos.
- **`appmanager.py`**: Interface para gerenciar produtos (cadastrar, editar, remover).
- **`order.py`**: Interface para adicionar produtos ao carrinho e finalizar compras.
- **`payment.py`**: Interface para processar pagamentos.
- **`database.py`**: Script para manipulação do banco de dados.
- **`Sistem.bd`**: Arquivo do banco de dados SQLite3.
- **`screen.py`**: Funções auxiliares para a interface gráfica.
- **`main.py`**: Ponto de entrada do aplicativo.

---
