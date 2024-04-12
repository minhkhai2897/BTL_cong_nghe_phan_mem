import os
from _score import Score
from _helper_for_score import STORAGE_PATH, STORAGE_RANKLIST_NUM


class Ranklist(Score):
    def __init__(self):
        self._len_list = 0
        self._list_scores = []

    def read_score(self, f, score: Score): 
        """Đọc các số damage, stand,... từ file stream f và lưu vào score để tính score"""
        line = f.readline().strip()
        if line:
            score_values = list(map(int, line.split()))  
            score.add_new_score_for_test(*score_values) 
            score.calculate_score()

    def write_score(self, f, score: Score):
        f.write(f"{score._damage} {score._stand} {score._killed} {score._got}\n")

    def destroy_ranklist(self):
        for score in self._list_scores:
            score.destroy_score()

    def insert_score_to_ranklist(self, score: Score) -> list[Score]:
        for i in range(0, self._len_list):
            if self._list_scores[i]._rank < score._rank:
                if self._len_list < STORAGE_RANKLIST_NUM:
                    """Ranklist vẫn chưa max thì tạo slot cho score"""
                    self._list_scores.append(Score())
                else: self._list_scores[-1].destroy_score()

                """Nếu như Ranklist đã max thì chèn score vào Ranklist theo đúng rank"""
                for j in range(self._len_list , i, -1):
                    self._list_scores[j] = self._list_scores[j - 1]
                self._list_scores[i] = Score()
                self._list_scores[i].add_new_score(score)
                self._len_list += 1
                break
        return self._list_scores 
    
    def write_ranklist(self, path):
        """Ghi các score vào ranklist"""
        with open(path, "w") as f:
            f.write(f"{self._len_list}\n") # ghi số lượng score có trong ranklist đầu tiên
            for score in self._list_scores:
                self.write_score(f, score)
            
            
    
    def read_ranklist(self, path) -> list[Score]:
        """Đọc ranklist từ file stream f và lưu vào list scores"""
        with open(path, "r") as f:
            if not os.path.exists(path):
                self._len_list = 1
                self._list_scores = [Score()]
                return self._list_scores
            

            self._len_list = (f.readline().strip())
            
            if len(self._len_list) == 0:  
                self._len_list = 1
            self._len_list = int(self._len_list)

            for i in range(self._len_list):
                self._list_scores.append(Score())
                self.read_score(f, self._list_scores[i])
            return self._list_scores

    def update_local_ranklist(self, score: Score):
        self.read_ranklist(STORAGE_PATH)
        score.calculate_score()
        self.insert_score_to_ranklist(score)

        for score in self._list_scores:
            print(score.to_list())

        print(self._len_list)

        self.write_ranklist(STORAGE_PATH)