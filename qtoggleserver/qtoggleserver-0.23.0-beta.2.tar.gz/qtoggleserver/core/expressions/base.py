
from __future__ import annotations

import abc

from typing import Optional, Set


class Expression(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eval(self) -> float:
        raise NotImplementedError()

    def get_deps(self) -> Set[str]:
        # Special deps:
        #  * 'time' - used to indicate dependency on system time (seconds)
        #  * 'time_ms' - used to indicate dependency on system time (milliseconds)

        return set()

    @staticmethod
    @abc.abstractmethod
    def parse(self_port_id: Optional[str], sexpression: str, pos: int) -> Expression:
        raise NotImplementedError()
