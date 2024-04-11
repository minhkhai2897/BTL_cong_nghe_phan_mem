#68 - game_level
import pdb


class Score:
    def __init__(self):
        """ got: chiều dài snake
            stand: thời gian sinh tồn"""
        self._damage = 0
        self._stand = 0
        self._killed = 0
        self._got = 0
        self._rank = 0.0

    def destroy_score(self):
        del self
    
    def calculate_score(self):
        if self.got == 0:
            self.rank
            return
        
        game_level = 0 # cần chỉnh sửa

        self.rank = (self.damage / self.got +
                    self.stand / self.got +
                    self.got * 50 + 
                    self.killed * 100)
        self.rank *= game_level + 1

    def add_score(self, other):
        self.damage += other.damage
        self.stand += other.stand
        self.killed += other.killed
        self.got += other.got
        self.calculate_score()

    def add_new_score(self, other):
        self.damage = other.damage
        self.stand = other.stand
        self.killed = other.killed
        self.got = other.got
        