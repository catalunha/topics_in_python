Antes de iniciar qualquer trabalho no google colab inicie esta biblioteca para habilitar verificação de tipos das variáveis 
```py
if "google.colab" in str(get_ipython()):
    !pip install nb-mypy -qqq
%load_ext nb_mypy
```

Documentação em:
https://colab.research.google.com/github/ssciwr/lunch-time-python/blob/main/lunchtime9/lunchtime9.ipynb#scrollTo=9

https://pypi.org/project/nb-mypy/
