'''
https://www.codewars.com/kata/5526fc09a1bbd946250002dc/
'''

def find_outlier(integers):
    odd_even = [num % 2 for num in integers]
    result = None
    if odd_even.count(0) == 1:
        result = integers[odd_even.index(0)]
    elif odd_even.count(1) == 1:
        result = integers[odd_even.index(1)]
    return result


if __name__ == "__main__":
    print(find_outlier([2, 4, 6, 8, 10, 3]), 3)
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)