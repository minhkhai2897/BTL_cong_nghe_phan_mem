import _storage
import _score



if __name__ == "__main__":
    # score1 = _score.Score()
    # score1.add_new_score_for_test(9714, 3705, 47, 29)

    score2 = _score.Score()
    score2.add_new_score_for_test(9024, 4664, 25, 22)

    # score3 = _score.Score()
    # score3.add_new_score_for_test(9024, 4664, 25, 22)

    ranklist = _storage.Ranklist()
    # ranklist.update_local_ranklist(score1)
    ranklist.update_local_ranklist(score2)
    # ranklist.update_local_ranklist(score3)
    
    