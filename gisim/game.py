'''Genius Invokation Game class
'''
from enum_classes import *
from numpy.random import RandomState
from collections import OrderedDict
from .player_area import PlayerArea
from .judge import Judge
    
class Game:
        
    def __init__(self, player1_deck:dict, player2_deck:dict, seed:int=50):
        self._random_state = RandomState(seed)
        self._status = GameStatus.INITIALIZING
        self._phase = Phase.CHANGE_CARD
        self._seed = seed
        self._active_player = self._random_state.choice([1, 2]) # Toss coin to determine who act first
        self.judge = Judge(self)
        self.player1_area = PlayerArea(self, self._random_state, player_id=PlayerID.PLAYER1, deck=player1_deck)
        self.player2_area = PlayerArea(self, self._random_state, player_id=PlayerID.PLAYER2, deck=player2_deck)
        

        
    def encode_game(self, viewer_id:PlayerID):
        assert viewer_id in [0, 1, 2], "viewer_id should be one of 0 (judge), 1, 2"
        return OrderedDict({'viewer_id': viewer_id, 'status':self._status, 'phase':self._phase,
                            'player1':self.player1_area.encode(viewer_id), 
                            'player2':self.player2_area.encode(viewer_id)})

    def get_random_state(self):
        return self._random_state