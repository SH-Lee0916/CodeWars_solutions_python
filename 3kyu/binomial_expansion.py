'''
https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b
'''
from math import factorial as facto
import re


def comb(n, i):
    return facto(n) // facto(i) // facto(n - i)

def expand(expr):
    equ, exp = expr.split("^")
    exp = int(exp)
    result = ""
    nums = list(re.findall(r"\-?[0-9\-]+|\+?[0-9]+", equ))
    alpha = re.findall(r"[a-zA-Z]+", equ)[0]
    if nums[0] == "-":
        nums[0] = "-1"
    elif len(nums) == 1:
        nums = ["1"] + nums
        
    nums = list(map(int, nums))
    
    if exp == 0:
        result = "1"
    elif exp == 1:
        if nums[0] < 0:
            if nums[0] != -1:
                result = f"-{abs(nums[0])}{alpha}{nums[1]}" if nums[1] < 0 else f"-{abs(nums[0])}{alpha}+{nums[1]}"
            else:
                result = f"-{alpha}{nums[1]}" if nums[1] < 0 else f"-{alpha}+{nums[1]}"
        if nums[0] > 0:
            if nums[0] != 1:
                result = f"{nums[0]}{alpha}{nums[1]}" if nums[1] < 0 else f"{nums[0]}{alpha}+{nums[1]}"
            else:
                result = f"{alpha}{nums[1]}" if nums[1] < 0 else f"{alpha}+{nums[1]}"
    else:
        for i, n in enumerate(range(exp, -1, -1)):
            if i != exp:
                f_num = comb(exp, i) * nums[0] ** (exp-i) * nums[1] ** i
                if f_num == 1 and f_num > 0:
                    f_num = ""
                elif f_num > 0 and i != 0:
                    f_num = f"+{f_num}"
                elif f_num == -1 and i == 0:
                    f_num = "-"
                
                exp_num = exp - i
                if exp_num == 1:
                    result += f"{f_num}{alpha}"
                else:
                    result += f"{f_num}{alpha}^{exp_num}"
                
            else:
                num = nums[1] ** exp
                if num > 0:
                    result += f"+{num}"
                else:
                    result += f"{num}"
    
    return result


if __name__ == "__main__":
    print(expand("(-x+1)^0"), "1")
    print(expand("(-x+1)^1"), "-x+1")
    print(expand("(x+1)^0"), "1")
    print(expand("(x+1)^1"), "x+1")
    print(expand("(x+1)^2"), "x^2+2x+1")

    print(expand("(x-1)^0"), "1")
    print(expand("(x-1)^1"), "x-1")
    print(expand("(x-1)^2"), "x^2-2x+1")

    print(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
    print(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
    print(expand("(7x-7)^0"), "1")

    print(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
    print(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
    print(expand("(-7x-7)^0"), "1")