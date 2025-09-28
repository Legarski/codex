from typing import Any, ClassVar, Tuple


class _TypedDictMeta(type):
    __orig_bases__: ClassVar[Tuple[Any, ...]]
