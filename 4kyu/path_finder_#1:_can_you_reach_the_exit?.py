'''
https://www.codewars.com/kata/5765870e190b1472ec0022a2/
'''
from collections import deque


def path_finder(maze):
    check_maze = [[ch for ch in row] for row in maze.split("\n")]
    mv_cand = deque([(0, 0)])
    maze_size = len(check_maze[0]) - 1
    target_pos = (maze_size, maze_size)
    flag = False
    
    while mv_cand:
        cur = mv_cand.pop()
        if cur == target_pos:
            flag = True
            break
        
        if check_maze[cur[0]][cur[1]] == "W":
            continue
        
        # West
        if cur[1] - 1 >= 0 and check_maze[cur[0]][cur[1] - 1] != "W":
            mv_cand.appendleft((cur[0], cur[1] - 1))
        # East
        if cur[1] + 1 <= maze_size and check_maze[cur[0]][cur[1] + 1] != "W":
            mv_cand.appendleft((cur[0], cur[1] + 1))
        # North
        if cur[0] - 1 >= 0 and check_maze[cur[0] - 1][cur[1]] != "W":
            mv_cand.appendleft((cur[0] - 1, cur[1]))
        # South
        if cur[0] + 1 <= maze_size and check_maze[cur[0] + 1][cur[1]] != "W":
            mv_cand.appendleft((cur[0] + 1, cur[1])) 
            
        
        check_maze[cur[0]][cur[1]] = "W"
    
    return flag


if __name__ == "__main__":
    a = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])
    print(path_finder(a), True)
    
    a = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...WW",
        "...W."])
    print(path_finder(a), False)
    
    a = "\n".join([
        "..W",
        ".W.",
        "W.."])
    print(path_finder(a), False)
    
    a = "\n".join([
        ".WWWW",
        ".W...",
        ".W.W.",
        ".W.W.",
        "...W."])
    print(path_finder(a), True)
    
    a = "\n".join([
        ".W...",
        "W....",
        ".....",
        ".....",
        "....."])
    print(path_finder(a), False)
    
    a = "\n".join([
        ".W",
        "W."])
    print(path_finder(a), False)