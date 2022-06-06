'''
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/
'''

def descending_order(num):
    max_num = list(str(num))
    max_num.sort(key = lambda x: -int(x))
    return int("".join(max_num))
    
    
if __name__ == "__main__":
    print(descending_order(0), 0)
    print(descending_order(15), 51)
    print(descending_order(123456789), 987654321)