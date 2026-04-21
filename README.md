# 🧠 GymControl

---

## 👥 Integrantes

- João Pedro Zaidman dos Santos Gonçalves - 2320464

---

### ✨ Funcionalidades principais:
- Cadastro de usuários
- Login e logout
- Recuperação de senha
- Criação de treinos
- Edição/deldeção dos treinos
- Visualização personalizada por usuário

## 📌 Descrição do Projeto

O GymControl é um sistema web desenvolvido com Django que permite o gerenciamento de treinos de usuários.
O sistema possui autenticação, controle de acesso por tipo de usuário (comum e administrador) e permite a criação, visualização e gerenciamento de treinos e exercícios.

## 🌐 Publicação

👉 **Link do site:** [GymControl](https://inf-1407-trab1.vercel.app/)  

---

## 📖 Manual do Usuário

### 🔐 Login

Para fazer login, na página inicial clique em **"Login"**, onde será necessário preencher seu **usuário** e **senha**.

Caso você não tenha uma conta, clique em **"Criar uma conta"** no link localizado na parte de baixo da página.

---

### 📝 Cadastro

Para criar uma conta, você deve preencher os seguintes campos:
- Username
- Email
- Senha
- Confirmação de senha

A confirmação de senha é necessária para garantir que os dados foram preenchidos corretamente.

Os requisitos para username e senha são exibidos em inglês na própria página.

---

### 🏋️ Visualização de Treinos

Para visualizar seus treinos, a partir da página inicial você pode:
- Clicar em **"Treinos"** na barra superior, ou
- Clicar em **"Ver treinos"** no centro da homepage

Na página de treinos estarão listados os treinos cadastrados no seu nome.

Caso não haja nenhum treino, será necessário aguardar um administrador cadastrar um para você.

---

### 📋 Visualização de Exercícios

Para visualizar os exercícios de um treino:
- Clique no nome do treino desejado

Na página de exercícios, você verá:
- Quantidade de séries
- Quantidade de repetições

Além disso:
- Ao clicar no nome do exercício, você será redirecionado para um vídeo no YouTube demonstrando sua execução

---

## 🛠️ Funcionalidades do Administrador

### 🔑 Acesso como Admin

Para acessar como administrador:
- Vá até a página de login
- Utilize:
  - **Usuário:** admin  
  - **Senha:** admin123  

---

### 👥 Gerenciamento de Usuários e Treinos

Após o login como administrador:

- Acesse a página de **treinos**, onde estarão listados os usuários
- Clique no nome de um usuário para gerenciar seus treinos

Para criar um treino:
- Clique em **"Criar treino"** na seção de treinos do usuário

Você também pode:
- Editar o nome de um treino
- Deletar um treino

---

### 🏃 Gerenciamento de Exercícios

Para adicionar exercícios a um treino:

- Clique no treino desejado
- Clique em **"Adicionar exercício"**

Na criação do exercício:
- Escolha um exercício pré-cadastrado no banco
- Defina:
  - Quantidade de séries
  - Quantidade de repetições

---

### ✅ Testes Realizados

- Cadastro de usuários funcionando corretamente
- Login e logout funcionando
- CRUD de treinos funcionando
- Associação de exercícios aos treinos funcionando
- Redirecionamento para vídeos funcionando

### ❌ Limitações

- Formularios padrão em ingles (não foram traduzidos) 
- recuperação de senha em produção não envia email (apesar de não ser necessario)