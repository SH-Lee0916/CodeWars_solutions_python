'''
https://www.codewars.com/kata/546d15cebed2e10334000ed9/
'''
import re


def solve_runes(runes):
    left, right = runes.split("=")
    nums = list(re.findall(r"(-?[0-9?]+)([-+*])(-?[0-9?]+)", left)[0])
    op = nums[1]
    nums = [nums[0], nums[2], right]
    result = -1
    
    search = set("0123456789") - set(num for num in runes if num.isnumeric())
    
    if any(len(num) > 1 and num[0] == "?" if num[0] != "-" else len(num) > 1 and num[1] == "?" for num in nums ):
        search -= {"0"}
    
    for idx in sorted(search):
        tmp_nums = [num.replace("?", idx) for num in nums]
        if eval(tmp_nums[0] + op + tmp_nums[1]) == int(tmp_nums[2]):
            result = int(idx)
            break
            
    return result


if __name__ == "__main__":
    print(solve_runes("1+1=?"), 2, "Answer for expression '1+1=?' ");
    print(solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' ");
    print(solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' ");
    print(solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' ");
    print(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ");
    print(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ");
    print(solve_runes("??*1=??"), 2, "Answer for expression '??*11=??' ");