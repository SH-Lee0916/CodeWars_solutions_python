'''
https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python
'''

def valid_check(puzzle, pos, num):
    flag = True
    
    # Check row
    for idx in range(9):
        if num == puzzle[pos[0]][idx] and idx != pos[1]:
            flag = False
    
    # Check col
    for idx in range(9):
        if num == puzzle[idx][pos[1]] and idx != pos[0]:
            flag = False
    
    # Check block
    r_std = pos[0] // 3
    c_std = pos[1] // 3
    
    for r_idx in range(r_std * 3, (r_std + 1) * 3):
        for c_idx in range(c_std * 3, (c_std + 1) * 3):
            if [r_idx, c_idx] != pos and puzzle[r_idx][c_idx] == num:
                flag = False
            
    return flag


def sudoku(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    puzzle[row][col] = num
                    if valid_check(puzzle, [row, col], num):
                        if sudoku(puzzle):
                            return puzzle
                        else:
                            puzzle[row][col] = 0
                    else:
                        puzzle[row][col] = 0
                return False
    
    return puzzle


if __name__ == "__main__":
    unsolved = [[5,3,0,0,7,0,0,0,0],
                [6,0,0,1,9,5,0,0,0],
                [0,9,8,0,0,0,0,6,0],
                [8,0,0,0,6,0,0,0,3],
                [4,0,0,8,0,3,0,0,1],
                [7,0,0,0,2,0,0,0,6],
                [0,6,0,0,0,0,2,8,0],
                [0,0,0,4,1,9,0,0,5],
                [0,0,0,0,8,0,0,7,9]]
    
    print(sudoku(unsolved))