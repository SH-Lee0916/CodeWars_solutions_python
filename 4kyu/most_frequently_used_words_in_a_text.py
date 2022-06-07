'''
https://www.codewars.com/kata/51e056fe544cf36c410000fb/
'''

import re

def top_3_words(text):
    cnt ={}
    for word in re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())):
        word = word.strip().lower()
        if word and word in cnt.keys():
            cnt[word] = cnt[word] + 1
        elif word and word not in cnt.keys():
            cnt[word] = 1
    
    # print(cnt)
    cnt = sorted(cnt, key = lambda k: (cnt[k], k), reverse = True)
    
    return cnt[:3]


if __name__ == "__main__":
    print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
    print(top_3_words("  //wont won't won't "), ["won't", "wont"])
    print(top_3_words("  , e   .. "), ["e"])
    print(top_3_words("  ...  "), [])
    print(top_3_words("  '  "), [])
    print(top_3_words("  '''  "), [])
    print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])