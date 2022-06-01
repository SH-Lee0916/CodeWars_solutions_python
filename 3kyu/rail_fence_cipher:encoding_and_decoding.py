'''
https://www.codewars.com/kata/58c5577d61aefcf3ff000081
'''

def _generator(string):
    for ch in string:
        yield ch


def encode_rail_fence_cipher(string, n):
    result = ""
    tmp_result = [""] * n
    gen = _generator(string)
    try:
        for idx in range(0, len(string)):
            for tmp_idx in range(n):
                tmp_result[tmp_idx] += next(gen)
                
            for tmp_idx in range(n - 2, 0, -1):
                tmp_result[tmp_idx] += next(gen)
    except StopIteration:
        result = "".join(tmp_result)
    
    return result
    
    
def decode_rail_fence_cipher(string, n):
    result = ""
    
    tmp_result = []
    for idx in range(n):
        tmp_result.append([])
    gen = _generator([str(num) for num in range(len(string))])
    try:
        for idx in range(0, len(string)):
            for tmp_idx in range(n):
                tmp_result[tmp_idx].append(int(next(gen)))
                
            for tmp_idx in range(n - 2, 0, -1):
                tmp_result[tmp_idx].append(int(next(gen)))
    except StopIteration:
        tmp_result = [num for tmp in tmp_result for num in tmp]
        result = "".join([string[tmp_result.index(ch)] for ch in range(len(string))])
    
    return result


if __name__ == "__main__":
    # Encode
    print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN")
    print(encode_rail_fence_cipher("Hello, World!", 3) == "Hoo!el,Wrdl l")
    print(encode_rail_fence_cipher("Hello, World!", 4) == "H !e,Wdloollr")
    print(encode_rail_fence_cipher("", 3) == "")
    
    # Decode
    print(decode_rail_fence_cipher("H !e,Wdloollr", 4) == "Hello, World!")
    print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) == "WEAREDISCOVEREDFLEEATONCE")
    print(decode_rail_fence_cipher("", 3) == "")
    
    
    # test = "WEAREDISCOVEREDFLEEATONCE"
    # print(len(test))
    
    # gen = _generator(test)
    # print(gen)
    # print(next(gen))
    # print(next(gen))