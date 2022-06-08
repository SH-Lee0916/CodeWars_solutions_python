'''
https://www.codewars.com/kata/54b72c16cd7f5154e9000457
'''

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
              '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
              '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
              '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
              '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', 
              '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', 
              '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", 
              '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', 
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', 
              '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decode_bits(bits):
    bits = bits.strip("0")
    unit = min([len(length) for length in bits.split("1") + bits.split("0") if length]) # Awesome ref: https://github.com/8fdafs2/Codewars-Solu-Python/blob/master/src/kyu4_Decode_the_Morse_Code_Advanced.py
    
    bits_dicts = {"1" * unit: ".", "111" * unit: "-"}
    word_bits = bits.split("0000000" * unit)
    words = []
    for word_bit in word_bits:
        dot_dash_chs = []
        for characters in word_bit.split("000" * unit):
            chs = []
            for ch in characters.split("0" * unit):
                if ch:
                    chs.append(bits_dicts[ch])
            dot_dash_chs.append("".join(chs))
            
        words.append(" ".join(dot_dash_chs))
    
    return "   ".join(words)

def decode_morse(morse_code):
    result = []
    morse_words = morse_code.split("   ")
    for morse_word in morse_words:
        word = ""
        tmp_alpha = morse_word.split(" ")
        for code in tmp_alpha:
            if code:
                word += MORSE_CODE[code]
        if word:
            result.append(word)
    
    return " ".join(result)


if __name__ == "__main__":
    print(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')), 'HEY JUDE')
    print(decode_morse(decode_bits('01110')), "E")
