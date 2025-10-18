from typing import Protocol
class Interface(Protocol):
    __name: str
    def get_name(self):...