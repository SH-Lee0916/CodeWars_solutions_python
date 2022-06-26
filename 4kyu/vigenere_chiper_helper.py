'''
https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/
'''

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alpha = alphabet
        self.key = key
    
    def encode(self, text):
        result = ""
        for idx, ch in enumerate([ch for ch in text]):
            if ch in self.alpha:
                key_ch = self.key[idx % len(self.key)]
                result += self.alpha[(self.alpha.index(ch) + self.alpha.index(key_ch)) % len(self.alpha)]
            else:
                result += ch
        return result
    
    def decode(self, text):
        result = ""
        for idx, ch in enumerate([ch for ch in text]):
            if ch in self.alpha:
                key_ch = self.key[idx % len(self.key)]
                result += self.alpha[(self.alpha.index(ch) - self.alpha.index(key_ch)) % len(self.alpha)]
            else:
                result += ch
        return result


if __name__ == "__main__":
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)

    print(c.encode('codewars'), 'rovwsoiv')
    print(c.decode('rovwsoiv'), 'codewars')

    print(c.encode('waffles'), 'laxxhsj')
    print(c.decode('laxxhsj'), 'waffles')

    print(c.encode('CODEWARS'), 'CODEWARS')
    print(c.decode('CODEWARS'), 'CODEWARS')