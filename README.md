# 🚀 MiniPix Web - Sistema de Transferências Full-Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

Este projeto nasceu como um simples script de terminal em Python e evoluiu para uma **aplicação Full-Stack** baseada na arquitetura REST. O objetivo principal foi compreender na prática a comunicação assíncrona entre Cliente e Servidor, manipulação de métodos HTTP (GET/POST), resolução de CORS e deploy em infraestrutura Cloud.

## 🔗 Links do Projeto

- **Aplicação Web (Frontend):** [Clique aqui para acessar o MiniPix](https://zack-rodrigues.github.io/sistema-pix/) *(Hospedado no GitHub Pages)*
- **API (Backend):** `https://sistema-pix.onrender.com/` *(Hospedada no Render)*

---

## 💡 Funcionalidades

- **Listagem Dinâmica de Contas:** Consome os dados da API via método `GET` e renderiza a tabela de saldos em tempo real.
- **Transferências (Mock de Pix):** Realiza validações de saldo e conta inexistente através do método `POST`.
- **Persistência de Dados:** O backend utiliza manipulação de arquivos `.json` nativos do Python para garantir que os saldos não sejam perdidos após o reinício do servidor.
- **Feedback Assíncrono:** Interface não precisa ser recarregada. Mensagens de sucesso ou erro são tratadas no DOM via JavaScript Vanilla.

---

## 🛠️ Tecnologias e Arquitetura

### Frontend (Client-Side)
- **HTML5 & CSS:** Estruturação da interface de usuário.
- **JavaScript (Vanilla):** Uso da `Fetch API` para requisições assíncronas (Promises) e manipulação do DOM.

### Backend (Server-Side)
- **Python 3:** Linguagem principal da regra de negócios.
- **FastAPI:** Framework moderno e de alta performance para a construção da API RESTful.
- **Uvicorn:** Servidor ASGI para rodar a aplicação web.
- **CORSMiddleware:** Configuração de segurança para permitir requisições de origens cruzadas (Cross-Origin Resource Sharing) provenientes do GitHub Pages.

---

## ⚙️ Como executar o projeto localmente

Caso queira rodar o ambiente de desenvolvimento na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/zack-rodrigues/sistema-pix.git
   cd sistema-pix
   ```

2. **Instale as dependências do Backend:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicie o servidor local:**
   ```bash
   python -m uvicorn api:app --reload
   ```

4. **Abra o Frontend:**
   Basta abrir o arquivo `index.html` em qualquer navegador. *(Nota: para testes locais, lembre-se de alterar as URLs do `fetch` no JavaScript para `http://127.0.0.1:8000`).*

---

## 🧠 Aprendizados Destacados

- **Separação de Responsabilidades:** O frontend apenas exibe dados e coleta interações, enquanto o backend detém a regra de negócios totalitária.
- **Tratamento de Erros:** Lidando com respostas de erro (ex: `405 Method Not Allowed`) e roteamento de Endpoints (`/` vs `/transferir`).
- **Cloud Deploy:** Preparação do ambiente Python via `requirements.txt` e deploy automatizado (PaaS).

---
**Desenvolvido por Zack Rodrigues** 👨‍💻
