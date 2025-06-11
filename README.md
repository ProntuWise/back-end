# ProntuWise - Sistema de Gestão de Prontuários Médicos

## 📋 Sobre o Projeto

ProntuWise é um sistema de gestão de prontuários médicos desenvolvido com FastAPI. O sistema oferece funcionalidades para gerenciamento de pacientes, médicos, agendamentos e prontuários médicos, com foco em segurança e eficiência.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **PyJWT** - Autenticação via tokens JWT
- **Uvicorn** - Servidor ASGI
- **Pytest** - Framework de testes
- **OpenAI** - Integração com IA
- **PyPDF2** - Manipulação de arquivos PDF

## 🏗️ Estrutura do Projeto

```
.
├── alembic/            # Migrações do banco de dados
├── docs/              # Documentação do projeto
├── src/
│   ├── entities/     # Entidades do domínio
│   ├── enums/        # Enumerações
│   ├── models/       # Modelos do banco de dados
│   ├── repositories/ # Camada de acesso a dados
│   ├── routes/       # Rotas da API
│   ├── schemas/      # Schemas de validação
│   ├── services/     # Lógica de negócio
│   ├── tests/        # Testes automatizados
│   └── utils/        # Utilitários e helpers
├── main.py           # Ponto de entrada da aplicação
└── requirements.txt  # Dependências do projeto
```

## 🛠️ Configuração do Ambiente

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```env
DATABASE_URL=sua_url_do_banco
JWT_SECRET=seu_segredo_jwt
```

## 🚀 Executando o Projeto

1. Execute as migrações do banco de dados:
```bash
alembic upgrade head
```

2. Inicie o servidor:
```bash
python main.py
```
O servidor estará disponível em `http://localhost:8000`

## 📚 Documentação da API

Após iniciar o servidor, acesse:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔐 Autenticação

O sistema utiliza autenticação JWT (JSON Web Token). Para acessar endpoints protegidos:

1. Faça login através do endpoint `/auth/login`
2. Use o token retornado no header `Authorization: Bearer {token}`

## 👥 Níveis de Acesso

- **Admin**: Acesso total ao sistema
- **Doctor**: Acesso a prontuários e consultas
- **Unique_Secretary**: Secretário(a) dedicado(a) a um médico
- **General_Secretary**: Secretário(a) com acesso geral
- **Full**: Acesso completo ao sistema

## 🧪 Testes

Execute os testes com:
```bash
pytest
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 👨‍💻 Desenvolvedores

### Time de Desenvolvimento

- **Gabriel Merola** - Desenvolvedor Back-End
  - GitHub: [github.com/gabrielmerola]
  - Responsabilidades:
    - Arquitetura do Sistema
    - Desenvolvimento Backend (FastAPI)
    - Implementação de Autenticação e Segurança
    - Desenvolvimento de APIs RESTful
    - Integração com OpenAI
    - Implementação TDD e BDD

- **João Galhardo** - Desenvolvedor Back-End
  - Github: [github.com/]
  - Responsabilidades:
    - Desenvolvimento Backend (FastAPI)
    - Implementação do Banco de Dados
    - Desenvolvimento de APIs RESTful

- **Isaias CB Luz** - Desenvolvedor Full Stack
  - Github: [github.com/IsaiasCBLuz]
  - Responsabilidades:
    - Design do Banco de Dados
    - Desenvolvimento Backend (FastAPI)
    - Desenvolvimento de APIs RESTful
