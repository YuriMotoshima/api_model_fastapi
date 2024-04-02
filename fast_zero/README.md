```sh
All project is reference about this (https://fastapidozero.dunossauro.com/)
```

# Passos de instalação de dependencias
```sh
poetry install  
poetry add fastapi uvicorn
poetry add --group dev pytest pytest-cov taskipy blue ruff httpx isort
```

# Passos de configuração das dependencias no toml
```sh
[tool.ruff]
line-length = 79
exclude = ['.venv', 'migrations']

[tool.isort]
profile = "black"
line_length = 79
extend_skip = ['migrations']

[tool.pytest.ini_options]
pythonpath = "."

[tool.blue]
extend-exclude = '(migrations/)'

[tool.taskipy.tasks]
lint = 'ruff . && blue --check . --diff'
format = 'blue .  && isort .'
run = 'uvicorn fast_zero.app:app --reload'
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_zero -vv'
post_test = 'coverage html'
```

# Passo a Passo de Execução

```sh
poetry shell
uvicorn fast_zero.app:app
>>> http://127.0.0.1:8000
```


# DB

# echo 'database.db' >> .gitignore


Instalando o Alembic e Criando a Primeira Migração
Antes de avançarmos, é importante entender o que são migrações de banco de dados e por que são úteis. As migrações são uma maneira de fazer alterações ou atualizações no banco de dados, como adicionar uma tabela ou uma coluna a uma tabela, ou alterar o tipo de dados de uma coluna. Elas são extremamente úteis, pois nos permitem manter o controle de todas as alterações feitas no esquema do banco de dados ao longo do tempo. Elas também nos permitem reverter para uma versão anterior do esquema do banco de dados, se necessário.

Caso nunca tenha trabalhado com Migrações
Agora, começaremos instalando o Alembic, que é uma ferramenta de migração de banco de dados para SQLAlchemy. Usaremos o Poetry para adicionar o Alembic ao nosso projeto:

$ Execução no terminal!

poetry add alembic
Após a instalação do Alembic, precisamos iniciá-lo em nosso projeto. O comando de inicialização criará um diretório migrations e um arquivo de configuração alembic.ini:

$ Execução no terminal!

alembic init migrations
Com isso, a estrutura do nosso projeto sofre algumas alterações e novos arquivos são criados:

```sh
.
├── .env
├── alembic.ini
├── fast_zero
│  ├── __init__.py
│  ├── app.py
│  ├── models.py
│  ├── schemas.py
│  └── settings.py
├── migrations
│  ├── env.py
│  ├── README
│  ├── script.py.mako
│  └── versions
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
   ├── __init__.py
   ├── conftest.py
   ├── test_app.py
   └── test_db.py
```


No arquivo alembic.ini: ficam as configurações gerais das nossas migrações. Na pasta migrations foram criados um arquivo chamado env.py, esse arquivo é responsável por como as migrações serão feitas, e o arquivo script.py.mako é um template para as novas migrações.

Criando uma migração automática
Com o Alembic devidamente instalado e iniciado, agora é o momento de gerar nossa primeira migração. Mas, antes disso, precisamos garantir que o Alembic consiga acessar nossas configurações e modelos corretamente. Para isso, faremos algumas alterações no arquivo migrations/env.py.

Neste arquivo, precisamos:

Importar as Settings do nosso arquivo settings.py e a Base dos nossos modelos.
Configurar a URL do SQLAlchemy para ser a mesma que definimos em Settings.
Verificar a existência do arquivo de configuração do Alembic e, se presente, lê-lo.
Definir os metadados de destino como Base.metadata, que é o que o Alembic utilizará para gerar automaticamente as migrações.