# Comparando list, tupple, set, dict

Item | list | tuple | set | dict
---|---|---|---|---
Criada com | list() | tuple()| set()| dict()
Criada vazia | list_1=()|tuple_1=()| set_1=set()|dict_1={}
Mutabilidade | Sim | Não | Sim, mas elementos imutáveis | Sim. Chave é imutável. Valor é mutável
Imutabilidade | Não | Sim | Sim, mas elementos imutáveis | Sim. Chave é imutável. Valor é mutável
Mantem ordem do elementos | Sim | Sim | Não | Sim
Permite valores duplicados | Sim | Sim | Não | Não para chaves
Sintaxe example | [1,'a'] | (1,'a') | {1,'a'} | {'a':'A','b':2,}
Sintaxe type | [Any] | (Any) | {Any} | {str:Any}
Indice | 0 | 0 | Sem indice | Indice é a chave
Adicionar elemento | append() | Não permite | add() | Use 'chave':valor ou update()
Remover elemento | pop() | Não permite | Permite. Mas randomicamente | pop('chave')
Ordenável | sort() | Não permite | Não permite | sorted()
Buscar elemento | index()| index() | Não permite | get('chave')
Reverte elementos | reverse() | Não permite | Não permite | Não permite
Contar elementos | count() |count() |count() |count() 













## Tutoriais:

https://www.naukri.com/code360/library/difference-between-list-tuple-set-and-dictionary-in-python

https://medium.com/@rajputgajanan50/differences-between-list-tuple-set-and-dictionary-in-python-ab47007a7cd9

https://www.scaler.com/topics/python/difference-between-dictionary-list-tuple-and-set-in-python/

https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/

https://byjus.com/gate/difference-between-list-tuple-set-and-dictionary-in-python/

https://testbook.com/key-differences/difference-between-list-tuple-set-and-dictionary-in-python
