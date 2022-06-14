'''
https://www.codewars.com/kata/54a91a4883a7de5d7800009c/
'''

def increment_string(strng):
    nums = ""
    str_list = list(strng)
    while str_list and str_list[-1].isdigit():
        nums += str_list.pop()
        
    if nums:
        ori_len = len(nums)
        nums = nums[::-1]
        nums = f"{int(nums) + 1}"
        if len(nums) < ori_len:
            nums = "0" * (ori_len - len(nums)) + nums
    else:
        nums = "1"
    
    return "".join(str_list) + nums


if __name__ == "__main__":
    print(increment_string("foo"), "foo1")
    print(increment_string("foobar001"), "foobar002")
    print(increment_string("foobar1"), "foobar2")
    print(increment_string("foobar00"), "foobar01")
    print(increment_string("foobar99"), "foobar100")
    print(increment_string("foobar099"), "foobar100")
    print(increment_string(""), "1")