'''
https://www.codewars.com/kata/530e15517bc88ac656000716
'''

def rot13(message):
    small_min = ord("a")
    small_max = ord("z")
    
    big_min = ord("A")
    big_max = ord("Z")
    
    new_msg = ""
    for ch in message:
        ch_ascii = ord(ch)
        if ch.isalpha() and ch.isupper():
            if ch_ascii + 13 > big_max:
                new_msg += f"{chr(big_min + ((ch_ascii + 13) - big_max) - 1)}"
            else:
                new_msg += f"{chr(ch_ascii + 13)}"
        elif ch.isalpha() and ch.islower():
            if ch_ascii + 13 > small_max:
                new_msg += f"{chr(small_min + ((ch_ascii + 13) - small_max) - 1)}"
            else:
                new_msg += f"{chr(ch_ascii + 13)}"
        else:
            new_msg += ch
            
    return new_msg

if __name__ == "__main__":
    print(rot13("test"), "grfg")
    print(rot13("Test"), "Grfg")
    print(rot13("wvcEVkId5KIMJjrW"), "jipRIxVq5XVZWweJ")