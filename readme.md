# API Django Ninja 🎯

Bem-vindo à API Django Ninja! Este projeto foi desenvolvido para facilitar operações CRUD sem interface gráfica, simulando um sistema de gestão de alunos em uma escola de Judô.

## 🚀 Como executar o projeto

### 1. Configuração do ambiente virtual
Antes de rodar a API, crie seu ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt


#Rodando o servidor
python manage.py runserver


#depois de rodar a nossa primeira urls é esta 
https://api-django-ninja.onrender.com/api/docs

Acesse a documentação da API pelo Swagger: https://api-django-ninja.onrender.com/api/docs

🔍 Endpoints disponíveis
GET /alunos/ - Lista todos os alunos cadastrados

POST /alunos/ - Adiciona um novo aluno

PUT /alunos/{id} - Atualiza informações de um aluno

DELETE /alunos/{id} - Remove um aluno

GET /progresso/ - Consulta o progresso das aulas

🛠 Tecnologias utilizadas
Django Ninja para criação da API

SQLite como banco de dados

Swagger/OpenAPI para documentação

📢 Contribuições
Caso tenha sugestões, envie um pull request!

📜 Licença
Este projeto é distribuído sob a licença MIT.


