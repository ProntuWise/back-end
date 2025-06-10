Feature: Gerenciamento de Usuários
    Como um administrador do sistema
    Eu quero poder cadastrar novos usuários
    Para dar acesso ao sistema para profissionais da clínica

    Scenario: Cadastrar um novo usuário médico
        Given que sou um administrador do sistema
        And tenho os dados do novo usuário
        And o nome é "Isaias Cano Bello da Luz"
        And o email é "isaias@gmail.com"
        And a senha é "ajdbhfuy498u31br89341&*#Y$*@#oihfweo"
        And o tipo de usuário é "Doctor"
        When eu cadastrar o usuário
        Then o usuário deve ser cadastrado com sucesso
        And os dados do usuário devem estar corretos

    Scenario: Deletar um usuário existente
        Given que sou um administrador do sistema
        And existe um usuário com ID 1
        When eu deletar o usuário
        Then o usuário deve ser removido com sucesso 