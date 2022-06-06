'''
https://www.codewars.com/kata/554b4ac871d6813a03000035/
'''

def high_and_low(numbers):
    split = [int(num) for num in numbers.split(" ")]
    result = f"{max(split)} {min(split)}"
    return result


if __name__ == "__main__":
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
    print(high_and_low("1 2 3"), "3 1")