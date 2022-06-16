'''
https://www.codewars.com/kata/5270d0d18625160ada0000e4
'''
score_board = {"111": 1000, "222": 200, "333": 300,
               "444": 400, "555": 500, "666": 600,
               "1": 100, "5": 50}

def score(dice):
    result_score = 0
    dice_s = "".join([str(num) for num in sorted(dice)])
    
    while any(key in dice_s for key in score_board.keys()):
        for key, val in score_board.items():
            if key in dice_s:
                dice_s = dice_s.replace(key, "", 1)
                result_score += val
                
    return result_score


# from collections import Counter


# def score(dice):
#     cnt = Counter(dice)
#     result_score = 0
    
#     for num, val in cnt.items():
#         if val >= 3:
#             if num == 1:
#                 result_score += 1000
#             else:
#                 result_score += num * 100
#             val -= 3
        
#         while val >= 1 and num == 1:
#             result_score += 100
#             val -= 1

#         while val >= 1 and num == 5:
#             result_score += 50
#             val -= 1
                
#     return result_score


if __name__ == "__main__":
    print( score( [2, 3, 4, 6, 2] ), 0)
    print( score(  [4, 4, 4, 3, 3] ), 400)
    print( score(  [2, 4, 4, 5, 4] ), 450)
