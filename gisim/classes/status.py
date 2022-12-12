from abc import ABC, abstractmethod

from .entity import Entity


class StatusEntity(Entity, ABC):
    def __init__(self, name: str, player_id: int, position: int):
        super().__init__()
        assert player_id in [1, 2], "The player_id should be either 1 or 2"
        assert position in [
            -1,
            0,
            1,
            2,
        ], "The position should be on of -1(team combat status), 0(left), 1(middle), 2(right)"
        self.player_id = player_id
        self.position = position
        self.name = name

    def encode(self):
        # TODO
        pass
