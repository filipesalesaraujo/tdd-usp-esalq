# Gerenciamento de Testes (TDD) I e II

Este repositório contém dois ambientes distintos para a execução dos serviços com `Docker Compose`. A estrutura é organizada em duas pastas:

## Como subir o ambientes

Para iniciar o ambiente que será utilizado durante a aula, siga os passos abaixo:

1. Execute o comando para subir os containers:

```bash
docker-compose up -d
```

2. Após o término da aula, para parar e remover os containers, execute:

```bash
docker-compose down
```

## Rodando os testes

1. Execute o comando no terminal do container:

```bash
pytest
```

## Observações

- Certifique-se de ter o Docker instalado na sua máquina antes de rodar os comandos.
- Para mais informações sobre o Docker, consulte os tutoriais disponibilizados para a aula.
- Sinta-se à vontade para consultar o ambiente referencial sempre que tiver dúvidas durante a aula.
