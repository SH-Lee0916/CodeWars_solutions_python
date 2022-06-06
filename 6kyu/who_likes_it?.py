'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/
'''

def likes(names):
    if not names:
        result = "no one likes this"
    elif len(names) == 1:
        result = f"{names[0]} likes this"
    elif len(names) < 4:
        result = f"{', '.join([name for name in names[:-1]])} and {names[-1]} like this"
    else:
        result = f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
    
    return result


if __name__ == "__main__":
    print(likes([]), 'no one likes this')
    print(likes(['Peter']), 'Peter likes this')
    print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')