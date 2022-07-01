'''
https://www.codewars.com/kata/526571aae218b8ee490006f4/
'''

import re

def count_bits(n):
    return len(re.sub(r"0", "", bin(n)[2:]))


if __name__ == "__main__":
    print(count_bits(0), 0)
    print(count_bits(4), 1)
    print(count_bits(7), 3)
    print(count_bits(9), 2)
    print(count_bits(10), 2)