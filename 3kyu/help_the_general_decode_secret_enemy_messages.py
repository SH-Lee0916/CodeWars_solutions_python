'''
https://www.codewars.com/kata/52cf02cd825aef67070008fa/
'''

crypto = "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa"

def decode(s):
    decode_s = ""
    for idx, ch in enumerate(s):
        if ch in crypto:
            decode_s += crypto[(crypto.index(ch) - (idx + 1)) % 66]
        else:
            decode_s += ch
    
    return decode_s


if __name__ == "__main__":
    print(decode("atC5kcOuKAr!"), "Hello World!")