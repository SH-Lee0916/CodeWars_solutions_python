'''
https://www.codewars.com/kata/52c4dd683bfd3b434c000292
'''

def check(number, awesome_phrases):
    check = False
    if len(str(number)) > 2:
        if number % 100 == 0:
            check = True
        elif len(set(str(number))) == 1:
            check = True
        elif str(number) in "1234567890" or str(number) in "9876543210":
            check = True
        elif str(number) == str(number)[::-1]:
            check = True
        elif number in awesome_phrases:
            check = True
        
    return check


def is_interesting(number, awesome_phrases):
    result = 0
    # check zeros
    if check(number, awesome_phrases):
        result = 2
    elif check(number + 1, awesome_phrases) or check(number + 2, awesome_phrases):
        result = 1
            
    return result

if __name__ == "__main__":
    print(is_interesting(3, [1337, 256]), 0)
    print(is_interesting(1336, [1337, 256]), 1)
    print(is_interesting(1337, [1337, 256]), 2)
    print(is_interesting(11208, [1337, 256]), 0)
    print(is_interesting(11209, [1337, 256]), 1)
    print(is_interesting(11211, [1337, 256]), 2)
    print(is_interesting(99, []), 1)
    print(is_interesting(799999, []), 1)