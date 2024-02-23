from typing import Any

class FixedStack:

    class Empty(Exception):

        pass

    class Full(Exception):

        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None]* capacity
        self.capaity = capacity
        self.ptr = 0

    def __len__(self) -> int:

        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capaity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

