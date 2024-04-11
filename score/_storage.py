
import os
from ._score import Score
from ._helper import STORAGE_PATH, STORAGE_RANKLIST_NUM


class Ranklist(Score):
    def __init__(self, len_list: int):
        self._len_list = len_list

    def read_score(self, f, score: Score): 
        """Đọc các số damage, stand,... từ file stream f và lưu vào score để tính score"""
        line = f.readline().strip()
        if line:
            score = map(int, line.split())
            score.calculate_score()

    def write_score(self, f, score: Score):
        f.write(f"{score.damage} {score.stand} {score.killed} {score.got}\n")

    def destroy_ranklist(self, scores: list[Score]):
        for score in scores:
            score.destroy_score()

    def insert_score_to_ranklist(self, score: Score, scores: list[Score]) -> list[Score]:
        for i in range(0, self.len_list):
            if scores[i].rank < score.rank:
                if self.len_list < STORAGE_RANKLIST_NUM:
                    """Ranklist vẫn chưa max thì tạo slot cho score"""
                    scores.append(Score())
            else: scores[-1].destroy_score()
            """Nếu như Ranklist đã max thì chèn score vào Ranklist theo đúng rank"""
            for j in range(self.len_list - 1, i, -1):
                scores[j] = scores[j - 1]
            scores[i] = Score()
            score[i].add_new_score(score)
            break
        return scores
    
    def write_ranklist(self, path, scores: list[Score]):
        """Ghi các score vào ranklist"""
        with open(path, "w") as f:
            f.write(f"{self.len_list}\n") # ghi số lượng score có trong ranklist đầu tiên
            for score in scores:
                self.write_score(f, score)
    
    def read_ranklist(self, path) -> list[Score]:
        """Đọc ranklist từ file stream f và lưu vào list scores"""
        with open(path, "r") as f:
            if not os.path.exists(path):
                self.len_list = 1
                scores = []
                scores[0] = Score()
                return scores

            self.len_list = f.readline().strip()
            scores = []
            for i in range(self.len_list):
                scores[i] = Score()
                self.read_score(f, scores[i])
            return scores

    def update_local_ranklist(self, score: Score):
        scores = self.read_ranklist(STORAGE_PATH)
        scores = self.insert_score_to_ranklist(score, scores)
        self.write_ranklist(STORAGE_PATH, scores)

        



            
            

