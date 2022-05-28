'''
https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
'''

def spiralize(size):
    spiral = [[0 for idx in range(size)]] * size
    
    for line in range(size):
        if line == 0:
            spiral[0] = [1 for idx in range(size)]
            spiral = [list(sub) for sub in list(zip(*[sub_arr[::-1] for sub_arr in spiral]))]
        else:
            row = line // 4 * 2
            start_idx = (line - 1) // 4 * 2
            num_1 = size - ((line - 1) // 2 * 2)
            
            for idx in range(num_1):
                spiral[row][start_idx + idx] = 1
            
            spiral = [list(sub) for sub in list(zip(*[sub_arr[::-1] for sub_arr in spiral]))]
    
    while spiral[0][-3:] != [1, 0, 1]:
        spiral = [list(sub) for sub in list(zip(*[sub_arr[::-1] for sub_arr in spiral]))]
        
    spiral = [list(sub) for sub in list(zip(*[sub_arr[::-1] for sub_arr in spiral]))]
        
    return spiral


if __name__ == "__main__":
    from pprint import pprint
    pprint(spiralize(6))
    pprint([[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]])
    
    
    # pprint(spiralize(5))
    # print()
    # pprint([[1,1,1,1,1],
    #         [0,0,0,0,1],
    #         [1,1,1,0,1],
    #         [1,0,0,0,1],
    #         [1,1,1,1,1]])
    # print()
    # pprint(spiralize(8))
    # print()
    # pprint([[1,1,1,1,1,1,1,1],
    #         [0,0,0,0,0,0,0,1],
    #         [1,1,1,1,1,1,0,1],
    #         [1,0,0,0,0,1,0,1],
    #         [1,0,1,0,0,1,0,1],
    #         [1,0,1,1,1,1,0,1],
    #         [1,0,0,0,0,0,0,1],
    #         [1,1,1,1,1,1,1,1]])