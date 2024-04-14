#20
import _score

class PlayerType:
    def __init__(self):
        LOCAL = 0
        REMOTE = 1
        COMPUTER = 2

class Snake:
    """
    team: 
    player_type : người chơi hay máy
    """
    def __init__(self, move_step: int, team: int, player_type: PlayerType):
        self._move_step = move_step
        self._team = team
        self._score = _score.Score()
        self._player_type = player_type

    def create_snake(self, step: int, team: int, player_type: PlayerType):
        Snake.__init__(step, team, player_type)