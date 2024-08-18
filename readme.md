# Poetry para este projeto
Verificar se o python 3.12 esta ativo
  pyenv versions

Se nao estiver instalar com 

```
pyenv install 3.12.0
```

Marcar como o compilador local
```
pyenv local 3.12.0
```
Instalar poetry com 
```
poetry init

Would you like... no
Would you like... no
```
Conferindo se a pasta .venv foi criada. Senão verifique estas configs
```
poetry config --list

poetry config virtualenvs.create = true
poetry config virtualenvs.in-project = true
```

Ativar poetry a cada trabalho
```
poetry shell
```
Instalando pacotes
```
poetry add requests
```
Se já houver um pyproject.toml
Se assim que adicionar com poetry add ele não instalar. Apenas adicionar. Então tem que instalar após add.
```
poetry install
```


A referencia dos tópicos abordados neste material é:

0. (hello) Hello word
0. (comment) Comentários
0. (print) Imprimindo no terminal
0. (type) Tipos de variáveis e conversões
0. (dict) Dicionarios - dict
0. (list) Listas - list
0. (tuple) Tuplas - tuple
0. (set) Conjunto - set
0. (get) Caracteristicas em objetos
0. (args_) Usando args e **kwargs
0. (init1) Usando \_\_init\_\_.py para indicar pacote
0. (init2) Usando \_\_init\_\_() como construtor de classe
0. (name) Usando if \_\_name\_\_ == '\_\_main\_\_'
0. (flow) Controle e fluxo
0. (operators) Operadores aritméticos e relacionais
0. (functions) Funções
0. (class) Classes
0. (file) Lendo e escrevendo em arquivos
0. (try) Tratamento de exceções
0. (comprehensions) Criando Comprehensions
0. (lambda) Criando lambda
0. (json) Trabalhando com json's
0. (datetime) Trabalhando com datetime
0. (requests) Trabalhando com requests

# Script para criar pasta
mkdir requests; cd requests; touch readme.md; touch code_1.py

# Tutoriais
https://www.w3schools.com/python/default.asp


# CheatSheet
https://levelup.gitconnected.com/python-cheatsheet-5474e14853cb


#