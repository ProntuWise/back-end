Feature: Autenticação de Usuários
    Como um usuário do sistema
    Eu quero poder fazer login
    Para acessar as funcionalidades protegidas do sistema

    Scenario: Login com credenciais válidas
        Given que sou um usuário cadastrado no sistema
        And meu email é "John@gmail.com"
        And minha senha é "senha123"
        When eu tento fazer login
        Then o login deve ser bem-sucedido
        And devo receber um token de autenticação válido 