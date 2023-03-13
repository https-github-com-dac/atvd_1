
# Atividade Colaborativa 01  – Docker  

### Objetivos de aprendizagem

    ●   Saber identificar as características de uma image e container Docker.

    ●   Possuir um overview sobre os principais comandos e customizações.

    ●   Propor estratégias para manutenção de um sistema fazendo uso de containers.

### Metodologia

Esta atividade prática está planejada para ser executada em equipes (duas ou três pessoas) e em duas etapas. A primeira etapa será um levantamento teórico, onde cada equipe deve responder às cinco questões listadas no Teste de objetivos de aprendizagem (13/03/2023). As respostas devem estar em um arquivo no repositório. Por fim, a segunda etapa consiste em realizar a atividade prática descrita na Atividade Prática, esta também deve ser apresentada, explicando como foi desenvolvida (20/03/2023).
Todos os artefatos devem ser entregues em um repositório do Github e o link (apenas um link por equipe) adicionado à atividade no Google Classroom

### Teste de objetivos de aprendizagem

    1.  Qual a diferença entre image e container?
    2.  Qual a diferença entre os comandos COPY, EXPOSE e ADD?
    3.  Qual a diferença entre os comandos RUN, CMD e ENTRYPOINT?
    4.  Qual a diferença entre as estratégias de shell e exec?
    5.  Qual a diferença entre os comandos docker stop <container_id> e docker kill <container_id>? 

### Atividade prática

Desenvolva uma aplicação que realize as operações de CRUD para a entidade Livro e Editora. A funcionalidade precisa estar disponível com UI (interface para o usuário) com um template usável. A aplicação desenvolvida precisa estar disponível em contêiner. As demais informações de cadastro podem ser inseridas via script sql.

````java
class Livro{
    private int id; 
    private String titulo;
    private LocalDate dataDeLancamento;
} 
````

````java
class Editora{  
    private int codigo; 
    private String localDeOrigem;
    private String nomeFantasia;
}
````

### Requisitos

    ●   RF01 - Implementar classes de acesso aos dados (em memória e via JDBC);

    ●   RF02 - Criar as páginas para edição e listagem da entidade Livro;

    ●   RF03 - Criar as páginas para edição e listagem da entidade Editora;

    ●   RF04 - Criar uma página para realizar uma busca de Livro por titulo;

    ●   RF05 - Criar uma página para realizar uma busca de Editora por localDeOrigem;

    ●   RF06 - Realizar o deploy da aplicação no Docker usando uma das images do Payara.

    ●   RF07 - Realizar o deploy da aplicação usando o Docker Compose.

### Script do banco

O script para criação do banco.

````sql
CREATE TABLE livro(
    id serial PRIMARY KEY,
    titulo VARCHAR(80),
    dataDeLancamento DATE
);

````

````sql
CREATE TABLE editora(  
    codigo SERIAL PRIMARY KEY,
    localDeOrigem VARCHAR(100),
    nomeFantasia VARCHAR(100)
);
````
### Autores

- [@lyzzandro](https://www.github.com/lyzzandro)
- [@ivesfg1](https://github.com/ivesfg1)
- [@Jonathaannn](https://www.github.com/Jonathaannn)
