# plpred

By Christian Domingues Sanchez

a protein subcellular location prediction program

## Setup

```
$ make setup
```

## Estrutura do Projeto

- `environment.yml`: O arquivo environment é utilizado para realizar toda instalação e criar uma estrutura de ambiente pelo conda, com isto podemos criar ambientes isolados com as dependencias necessárias para a aplicação sem utilizar o sistema base como referencia do $Path
- `requeriments.txt`: Esse arquivo é a especificação de dependencias do Pip, por exemplo, onde podemos listar as bibliotecas do Python, com isso podemos realizar uma independencia maior do Python.
- `Makefile`: O make é utilizado para gerar regras e automatizar os comandos, rodando por exemplo uma regra setup, irá chamar a criação de ambiente e a atualização do mesmo.