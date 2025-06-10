Feature: Gerenciamento de Consultas
    Como um profissional da clínica
    Eu quero poder gerenciar consultas
    Para organizar os atendimentos dos pacientes

    Scenario: Criar uma nova consulta
        Given que sou um profissional da clínica
        And tenho os dados necessários para agendar uma consulta
        And a data escolhida é "2024-03-20"
        And o horário escolhido é "14:30"
        And a duração será de 30 minutos
        And o ID do paciente é 1
        And o ID do profissional é 1
        And o ID da tag é 1
        And a descrição é "Consulta de rotina"
        And o status é "Confirmed"
        And o tipo de consulta é "First_Visit"
        When eu criar a consulta
        Then a consulta deve ser criada com sucesso
        And os dados da consulta devem estar corretos

    Scenario: Listar todas as consultas
        Given que sou um profissional da clínica
        And existe pelo menos uma consulta cadastrada
        When eu solicitar a lista de consultas
        Then devo receber uma lista não vazia de consultas
        And os dados das consultas devem estar corretos 