'''
https://www.codewars.com/kata/550f22f4d758534c1100025a
'''

opposite_dir = {"NORTH": "SOUTH", 
                "SOUTH": "NORTH", 
                "EAST": "WEST", 
                "WEST": "EAST"}

def dirReduc(arr):
    stack = []
    for dir in arr:
        if stack and opposite_dir[dir] == stack[-1]:
            stack.pop()
        else:
            stack.append(dir)
            
    return stack


if __name__ == "__main__":
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(dirReduc(a), ['WEST'])
    u = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])