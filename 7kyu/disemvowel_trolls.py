'''
https://www.codewars.com/kata/52fba66badcd10859f00097e
'''

def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]
    for vow in vowels:
        string_ = string_.replace(vow, "")
        string_ = string_.replace(vow.upper(), "")
    return string_


if __name__ == "__main__":
    print(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")