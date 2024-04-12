#68 - game_level



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
        if self._got == 0:
            self._rank
            return
        
        game_level = 1 # cần chỉnh sửa

        self._rank = (self._damage / self._got +
                    self._stand / self._got +
                    self._got * 50 + 
                    self._killed * 100)
        self._rank *= game_level + 1

    def add_score(self, other):
        self._damage += other._damage
        self._stand += other._stand
        self._killed += other._killed
        self._got += other._got
        self.calculate_score()

    def add_new_score(self, other):
        """Cho một score mới vào 1 Score khởi tạo sẵn"""
        self._damage = other._damage
        self._stand  = other._stand
        self._killed = other._killed
        self._got    = other._got
    
    def add_new_score_for_test(self, damage: int, stand: int, killed: int, got: int):
        self._damage = damage
        self._stand  = stand
        self._killed = killed
        self._got    = got

    def to_list(self):
        return [self._damage, self._stand, self._killed, self._got]