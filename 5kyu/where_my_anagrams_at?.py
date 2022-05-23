'''
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
'''

def anagrams(word, words):
    return [ anagram for anagram in words if sorted(word) == sorted(anagram) ]


if __name__ == "__main__":
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])