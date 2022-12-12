from abc import ABCMeta, abstractmethod

from .entity import Entity


class Support(Entity, ABCMeta):
    def __init__(self, name: str, player_id: int):
        super().__init__()
        assert player_id in [1, 2]
        self.PLAYER_ID = player_id
        self.NAME = name

    def encode(self):
        # TODO
        pass
