'''
https://www.codewars.com/kata/546e2562b03326a88e000020
'''

def square_digits(num):
    return int("".join([str(int(each_num) ** 2) for each_num in str(num)]))
    
if __name__ == "__main__":
    print(square_digits(9119), 811181)
    print(square_digits(0), 0)