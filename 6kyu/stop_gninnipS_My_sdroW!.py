'''
https://www.codewars.com/kata/5264d2b162488dc400000001/
'''

def spin_words(sentence):
    tmp_words = sentence.split(" ")
    
    result_words = []
    for idx, words in enumerate(tmp_words):
        if len(words) >= 5:
            tmp_words[idx] = words[::-1]
            
    return " ".join(tmp_words)


if __name__ == "__main__":
    print(spin_words("Welcome"), "emocleW")
    print(spin_words("to"), "to")
    print(spin_words("CodeWars"), "sraWedoC")

    print(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
    print(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")