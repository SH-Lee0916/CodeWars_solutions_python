'''
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
'''

def zero(*args):
    if not args:
        retv = 0
    else:
        if type(args[0]) == str:
            retv = eval("0" + args[0])
    return retv

def one(*args):
    if not args:
        retv = 1
    else:
        if type(args[0]) == str:
            retv = eval("1" + args[0])
    return retv

def two(*args):
    if not args:
        retv = 2
    else:
        if type(args[0]) == str:
            retv = eval("2" + args[0])
    return retv

def three(*args):
    if not args:
        retv = 3
    else:
        if type(args[0]) == str:
            retv = eval("3" + args[0])
    return retv

def four(*args):
    if not args:
        retv = 4
    else:
        if type(args[0]) == str:
            retv = eval("4" + args[0])
    return retv

def five(*args):
    if not args:
        retv = 5
    else:
        if type(args[0]) == str:
            retv = eval("5" + args[0])
    return retv

def six(*args):
    if not args:
        retv = 6
    else:
        if type(args[0]) == str:
            retv = eval("6" + args[0])
    return retv

def seven(*args):
    if not args:
        retv = 7
    else:
        if type(args[0]) == str:
            retv = eval("7" + args[0])
    return retv

def eight(*args):
    if not args:
        retv = 8
    else:
        if type(args[0]) == str:
            retv = eval("8" + args[0])
    return retv

def nine(*args):
    if not args:
        retv = 9
    else:
        if type(args[0]) == str:
            retv = eval("9" + args[0])
    return retv


def plus(num):
    return f"+ {num}"

def minus(num):
    return f"- {num}"

def times(num):
    return f"* {num}"

def divided_by(num):
    return f"// {num}"

    

if __name__ == "__main__":
    print(seven(times(five())), 35)
    print(four(plus(nine())), 13)
    print(eight(minus(three())), 5)
    print(six(divided_by(two())), 3)