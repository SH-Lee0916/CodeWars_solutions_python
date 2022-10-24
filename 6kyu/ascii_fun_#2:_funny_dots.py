'''
https://www.codewars.com/kata/59098c39d8d24d12b6000020/python
'''

def dot(n, m):
    arr = []
    for row in range(2 * m + 1):
        if row % 2:
            arr.append("| o " * n + "|")
        else:
            arr.append("+---" * n + "+")
            
    return "\n".join(arr)


if __name__ == "__main__":
    print(dot(3, 2),  "\n+---+---+---+\n| o | o | o |\n+---+---+---+\n| o | o | o |\n+---+---+---+")