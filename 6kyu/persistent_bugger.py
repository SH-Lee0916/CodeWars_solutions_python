'''
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
'''

def persistence(n):
    cnt = 0
    if len(str(n)) > 1:
        nums = [ch for ch in str(n)]
        while len(nums) > 1:
            nums = [ch for ch in str(eval("*".join(nums)))]
            cnt += 1

    return cnt


if __name__ == "__main__":
    print(persistence(39), 3)
    print(persistence(4), 0)
    print(persistence(25), 2)
    print(persistence(999), 4)
