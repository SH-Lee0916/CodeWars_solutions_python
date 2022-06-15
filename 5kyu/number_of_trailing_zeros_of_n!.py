'''
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/python
'''

def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


if __name__ == "__main__":
    print(zeros(0), 0, "Testing with n = 0")
    print(zeros(6), 1, "Testing with n = 6")
    print(zeros(30), 7, "Testing with n = 30")