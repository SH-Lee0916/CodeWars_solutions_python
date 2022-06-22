'''
https://www.codewars.com/kata/537e18b6147aa838f600001b
'''

def justify(text, width):
    texts = text.split(" ")
    tmp_line = []
    tmp_line_len = 0
    lines = [tmp_line]
    result = []
    for word in texts:
        if tmp_line_len + len(word) > width:
            tmp_line = [word]
            lines.append(tmp_line)
            tmp_line_len = len(word) + 1
        else:
            tmp_line.append(word)
            tmp_line_len += len(word) + 1
            
    for line in lines[:-1]:
        if len(line) > 1:
            spaces = width - sum(len(word) for word in line)
            eq_spa = spaces // (len(line) - 1)
            rem_spa = spaces % (len(line) - 1)
            
            for idx, add_space in enumerate(range(rem_spa)):
                line[idx] = line[idx] + " "
                
            tmp_line = (" " * eq_spa).join(line)
            result.append(tmp_line)
        else:
            result.append("".join(line))
    
    result.append(" ".join(lines[-1]))
    return "\n".join(result)


if __name__ == "__main__":
    print(justify('123 45 6', 7))
    print(justify("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.""", 100))