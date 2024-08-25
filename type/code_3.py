"""
# Tipos especiais

Existem alguns tipos especiais que podem ser usados para especificar o tipo de dados de uma variável.

* Any: pode conter qualquer tipo de dados;
* Union: pode conter um dos tipos de dados especificados; Use Union[int, str] ou int | str
* Optional: pode conter um dos tipos de dados especificados ou None;
* Literal: pode conter um dos valores literais especificados;
* Final: pode especificar uma constante.
* Iterable: pode conter qualquer tipo de dados que possa ser iterado, ou seja, qualquer tipo de dados que possa ser usado em um loop for.
* Sequence: pode conter qualquer tipo de dados que possa ser indexado, ou seja, qualquer tipo que suporte à notação de colchetes;
* Mapping: pode conter qualquer tipo de dados que possa ser mapeado;
* MutableMapping: pode conter qualquer tipo de dados que possa ser mapeado e mutável;
* Callable: pode conter qualquer tipo de dados que possa ser chamado.
"""

from typing import (
    Any,
    Callable,
    Final,
    Iterable,
    Literal,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Union,
)

variavel_any: Any = 123
variavel_union: Union[int, str] = 123
variavel_optional: Optional[int] = 123
variavel_literal: Literal[1, 2, 3] = 1
variavel_final: Final = 123
variavel_iterable: Iterable[int] = [1, 2, 3]
variavel_sequence: Sequence[int] = [1, 2, 3]
variavel_mapping: Mapping[str, int] = {"a": 1, "b": 2, "c": 3}
variavel_mutable_mapping: MutableMapping[str, int] = {"a": 1, "b": 2, "c": 3}
variavel_callable: Callable[[int, int], int] = lambda x, y: x + y
