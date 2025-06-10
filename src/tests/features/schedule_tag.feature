Feature: Gerenciamento de Tags de Agendamento
    Como um administrador da clínica
    Eu quero poder criar tags para categorizar agendamentos
    Para melhor organizar os tipos de consulta

    Scenario: Criar uma nova tag de agendamento
        Given que sou um administrador da clínica
        And quero criar uma nova categoria de agendamento
        And o nome da tag é "Consulta Pediátrica"
        And a descrição da tag é "Agendamento para consultas pediátricas"
        When eu criar a tag de agendamento
        Then a tag deve ser criada com sucesso
        And deve ter um ID único
        And os dados da tag devem estar corretos 