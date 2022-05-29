'''
https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
'''

str2num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
           "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
           "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
           "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, 
           "seventy": 70, "eighty": 80, "ninety": 90,
           "hundred": 100, "thousand": 1000, "million": 1000000}


def parse_int(string):
    num = 0
    string = string.replace("-", " ")
    string = string.replace(" and ", " ")
    
    chunks = string.split()
    print(list(reversed(chunks)))
    chunk_stack = []
    for chunk in reversed(chunks):
        if not chunk_stack:
            chunk_stack.append(chunk)
            continue

        if str2num[chunk_stack[0]] < str2num[chunk]:
            tmp_num = 0
            while chunk_stack:
                if chunk_stack[-1] in ["hundred", "thousand", "million"]:
                    tmp_num = tmp_num * str2num[chunk_stack.pop()]
                else:
                    tmp_num += str2num[chunk_stack.pop()]
            num += tmp_num
            chunk_stack.append(chunk)
        else:
            chunk_stack.append(chunk)
    
    tmp_num = 0
    while chunk_stack:
        if chunk_stack[-1] in ["hundred", "thousand", "million"]:
            tmp_num = tmp_num * str2num[chunk_stack.pop()]
        else:
            tmp_num += str2num[chunk_stack.pop()]
    num += tmp_num
    
    return num


if __name__ == "__main__":
    print(parse_int('one'), 1)
    print(parse_int('twenty'), 20)
    print(parse_int('two hundred forty-six'), 246)
    print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"), 783919)