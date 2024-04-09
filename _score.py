#68 - game_level
import pdb

STORAGE_RANKLIST_NUM = 10

class Score:
    def __init__(self):
        """ got: chiều dài snake
            stand: """
        self.damage = 0
        self.stand = 0
        self.killed = 0
        self.got = 0
        self.rank = 0.0

    def destroy_score(self):
        del self
    
    def calculate_score(self):
        if self.got == 0:
            self.rank
            return
        
        game_level = 0

        self.rank = (self.damage / self.got +
                    self.stand / self.got +
                    self.got * 50 + 
                    self.killed * 100)
        self.rank *= game_level + 1

    def add_score(a, b)
        a.got += b.got
        a.damage += b.damage
        a.killed += b.killed
        a.stand += b.stand
        calculate_score(a)