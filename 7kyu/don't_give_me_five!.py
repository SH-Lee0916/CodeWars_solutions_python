'''
https://www.codewars.com/kata/5813d19765d81c592200001a
'''

def dont_give_me_five(start, end):
    return sum(1 for idx in range(start, end + 1) if "5" not in str(idx))


if __name__ == "__main__":
    print(dont_give_me_five(1,9), 8)
    print(dont_give_me_five(4,17), 12)