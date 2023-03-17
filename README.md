Backend
===============

Instruções de Configuração
Atenção: crie todos os serviços na mesma região da AWS.

S3
  No console do S3 https://s3.console.aws.amazon.com/, crie um bucket:
  Insira o nome do bucket e anote-o.
  Clique em "Criar bucket".
  Dentro do bucket que você criou, clique em "Carregar".
  Adicione um arquivo .csv contendo os cabeçalhos "cpf", "cnpj" e "data", seguindo o arquivo dados.csv deste repositório.
  Clique em "Carregar".


Banco de Dados
  No console do RDS https://console.aws.amazon.com/rds, crie um banco de dados:
  Selecione "Criação padrão";
  Selecione "PostgreSQL";
  Selecione o modelo do Nível gratuito;
  Selecione instância de banco de dados única;
  Escolha o nome do usuário principal (padrão: "postgres"), e anote-o;
  Adicione uma senha principal, e anote-a;
  Selecione a opção "Classes com capacidade de intermitência" e selecione a opção "db.t3.micro";
  Permita o acesso público;
  Em "Configuração adicional", insira o nome do banco de dados inicial, e anote-o;
  Clique em "Criar banco de dados".
  Após a criação do banco, acesse a instância que você acabou de criar pelo console.

  Na seção "Segurança e Conexão", anote o endpoint da instância e a porta (por padrão, 5432).

Lambda

  No console do Lambda https://console.aws.amazon.com/lambda, crie uma função com Python 3.9 no tempo de execução.
  Após criada, acesse a função e crie um gatilho para invocá-la:
  Selecione "API Gateway" como origem;
  Crie uma nova API;
  Escolha uma API do tipo "REST API";
  Em segurança, selecione "API key";
  Clique em "Adicionar".
  Clique no gatilho criado e anote o API endpoint e a API key.
  Acesse a função e vá para a seção de "Configuração" e vá em "Variáveis de Ambiente".
  Adicione as seguintes variáveis de ambiente:
  AWS_DB_HOST -> é o endpoint da instância do banco de dados
  AWS_DB_NAME -> é o nome do banco de dados inicial
  AWS_DB_PASSWORD -> é a senha principal do usuário principal do banco de dados
  AWS_DB_PORT -> é a porta da instância do banco de dados
  AWS_DB_USER -> é o usuário principal do banco de dados
  USER_ACCESS_KEY -> é a AWS access key id de um usuário criado na sua conta da AWS
  USER_SECRET_ACCESS_KEY -> é a AWS secret access key de um usuário criado na sua conta da AWS
  Clone o projeto no GitHub, e em seguida crie um arquivo .zip contendo a pasta "app", a pasta "psycopg2" e o arquivo "lambda_function.py".
  Em seguida, no console da sua função lambda, na seção "Código", clique em "Fazer upload de arquivo .