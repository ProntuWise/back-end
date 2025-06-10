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

    Scenario: Alteração de senha
        Given que sou um usuário cadastrado no sistema
        And meu email é "John@gmail.com"
        And quero alterar minha senha
        When eu altero minha senha para "senha456"
        Then a senha deve ser alterada com sucesso 