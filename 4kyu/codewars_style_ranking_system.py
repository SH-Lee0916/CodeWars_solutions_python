'''
https://www.codewars.com/kata/51fda2d95d6efda45e00004e/
'''

ranks = (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8)    

class User():
    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    
    def __rankup(self):
        if self.rank < 8:
            cur_rank_idx = ranks.index(self.rank)
            
        self.rank = ranks[cur_rank_idx + 1]
    
        
    def __cal_progress(self, prob_rank):
        prob_rank_idx = ranks.index(prob_rank)
        cur_rank_idx = ranks.index(self.rank)
        
        if self.rank != 8:
            if prob_rank_idx + 1 == cur_rank_idx:
                self.progress += 1
            elif prob_rank_idx == cur_rank_idx:
                self.progress += 3
            elif prob_rank_idx > cur_rank_idx:
                d = prob_rank_idx - cur_rank_idx
                self.progress += 10 * d * d
                
            while self.progress >= 100:
                self.progress -= 100
                self.__rankup()
                if self.rank == 8:
                    self.progress = 0
    
        
    def inc_progress(self, prob_rank):
        self.__cal_progress(prob_rank)
        

if __name__ == "__main__":
    user = User()
    print(user.rank, -8)
    print(user.progress, 0)
    user.inc_progress(-7)
    print(user.progress, 10)
    user.inc_progress(-5)
    print(user.progress, 0)
    print(user.rank, -7)