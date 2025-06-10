Feature: Gerenciamento de Pacientes
    Como um profissional da clínica
    Eu quero poder cadastrar novos pacientes
    Para manter um registro dos atendimentos

    Scenario: Cadastrar um novo paciente
        Given que sou um profissional da clínica
        And tenho os dados do paciente para cadastro
        And o nome do paciente é "Maria Silva"
        And o CPF é "123.456.789-00"
        And o RG é "12.345.678-9"
        And a data de nascimento é "1990-05-15"
        And o telefone é "(11) 98765-4321"
        And o email é "maria.silva@email.com"
        And o endereço é "Rua das Flores, 123"
        And o gênero é "Female"
        And o caminho da pasta é "/pacientes/maria_silva"
        When eu cadastrar o paciente
        Then o paciente deve ser cadastrado com sucesso
        And deve ter um ID único
        And os dados do paciente devem estar corretos 