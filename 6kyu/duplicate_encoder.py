'''
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
'''
from collections import Counter


def duplicate_encode(word):
    cnt = Counter(word.lower())
    words = [ch for ch in word.lower()]
    for idx, ch in enumerate(words):
        if cnt[ch] > 1:
            words[idx] = ")"
        else:
            words[idx] = "("
    
    
    return "".join(words)
        


if __name__ == "__main__":
    print(duplicate_encode("din"),"(((")
    print(duplicate_encode("recede"),"()()()")
    print(duplicate_encode("Success"),")())())","should ignore case")
    print(duplicate_encode("(( @"),"))((")
    print(duplicate_encode(" ( ( )"), ")))))(")