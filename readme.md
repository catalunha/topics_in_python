# Tópicos em Python

Anotei aqui alguns tópicos em pyhton. Mas é importante consultar a documentação original da linguagem em:

0. https://www.python.org/

E também outras fontes:

0. https://www.w3schools.com/python/default.asp


## Sumário dos tópicos

Abordaremos:

0. (hello) Hello word
0. (comment) Comentários
0. (print) Imprimindo no terminal
0. (type) Tipos de variáveis e conversões
0. (list) Listas - list
0. (dict) Dicionarios - dict
0. (tuple) Tuplas - tuple
0. (set) Conjunto - set
0. (get) Caracteristicas em objetos
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
0. (args_) Usando args e **kwargs
0. (init_package) Usando \_\_init\_\_.py para indicar pacote
0. (init_class) Usando \_\_init\_\_() como construtor de classe
0. (name_main) Usando if \_\_name\_\_ == '\_\_main\_\_'

Meu Script para criar pasta
```
mkdir typing; cd typing; touch readme.md; touch code_1.py
```

## Ambiente de desenvolvimento

### Online
Poderemos usar o:

0. https://app.programiz.pro/
0. https://www.online-python.com/

### Linux
Ou instalar o ambiente localmente. Para Linux segue meu roteiro.

Verificar se o python 3.12 esta ativo
```
  pyenv versions
```

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

Instalando pacotes
```
poetry add requests
```
Se já houver um pyproject.toml use apenas o comando a seguir. Ou

Se assim que adicionar com poetry add ele não instalar. Apenas adicionar. Então tem que instalar após add.
```
poetry install
```

Ativar poetry a cada trabalho
```
poetry shell
```

No VSCode prescione: ctrl alt n

Instale as seguintes extensões:

![](images/extensions.png)

### Mac
Em construção.

### Win
Em construção.

