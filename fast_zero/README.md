# Passos de instalação de dependencias
poetry install  
poetry add fastapi uvicorn
poetry add --group dev pytest pytest-cov taskipy blue ruff httpx isort

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