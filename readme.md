[Introduction](#introduction) • [Entities](#entities) • [Endpoints made available](#endpoints-made-available) • [Technologies](#technologies) • [Documentation](#documentation) 

## Introduction

This API is part of the project to remotes experimentations using the system Brlab 1.0 to the IFNMG Campus Januária.

## Entities

The API has a total of 8 entities and each entity has endpoints to access information.

- Usuario
- Instituicao
- Equipamento
- Papel
- Convenio
- Agendamento
- Experimento
- Laboratorio

Obs: Neither all endpoints the entities were implemented until the moment

## Endpoints made available

The basis for accessing the api is https://api-brlab-v1.herokuapp.com

| Recurso | Endpoint | Description |
| :----------: | :----------------------: | :------------: |
| Labs | /labs/ | List all labs  |
| Labs | /labs/<int:lab_id> | List a specify lab |
| Usuarios | /usuarios | List all users |
| Usuario | /usuario/<int:user_id> | Return informations about a user |
| Instituicao | /instituicoes | List all institutions registred |
| Instituicao | /instituicao/<int:institution_id> | List a specify institution |
| Experimento | /experimento/<int:experimento_id> | Lists an experiment specified by id |
| ExperimentoByUsuario | /experimentos/usuario/<int:usuario_id> | Experiments performed by a specific user|
| Agendamentos | /agendamentos | Lists all appointments |
| AgendamentoByUsuario | /agendamento/usuario/<int:user_id> | Shows all user's appointments |

## Technologies

- Python version 3.7
- Flask 1.1.1
- Postgres 11.9
- Heroku
- Postman

## Documentation

The entire API and its endpoints were documented and tested using Postman.
The documentation, describing the accessible entities and terminals, is available at <https://documenter.getpostman.com/view/5404533/TVRq1RHu>.

<div style="display: flex;">
<img src="https://img.shields.io/static/v1?label=Python&message=3.7&color=3776AB&style=flat-square&logo=python" style="margin: 10px"/>
<img src="https://img.shields.io/static/v1?label=Flask&message=1.1.1&color=000&style=flat-square&logo=flask" style="margin: 10px"/>
<img src="https://img.shields.io/static/v1?label=PostgreSQL&message=11.9&color=336791&style=flat-square&logo=PostgreSQL" style="margin: 10px"/>
</div>
