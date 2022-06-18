'''

'''
import re

"r'0*((1(01*0)*1)*0*)*$'" # below is simplifying version 
PATTERN = re.compile(r"(1(01*0)*1|0)*$")


if __name__ == "__main__":
    tests = [(False, " 0" ),
        (False, "abc"),
        (True,  "000"),
        (True,  "110"),
        (False, "111"),
        (True,  "{:b}".format(12345678)),
       ]

    for exp,s in tests:
        print(bool(PATTERN.match(s)), exp)