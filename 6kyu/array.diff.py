'''
https://www.codewars.com/kata/523f5d21c841566fde000009/
'''

def array_diff(a, b):
    return [num for num in a if num not in b]
    
    
if __name__ == "__main__":
    print(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    print(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
    print(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    print(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
    print(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
    print(array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")