'''
https://www.codewars.com/kata/559a28007caad2ac4e000083
'''

def perimeter(n):
    result = 0

    if n == 0:
        result = 1
    elif n == 1:
        result = 2
    else:
        fibo = [1, 1]
        while len(fibo) < n + 1:
            fibo.append(fibo[-2] + fibo[-1])
        result = sum(fibo) * 4

    return result


if __name__ == "__main__":
    print(perimeter(5), 80)
    print(perimeter(7), 216)
    print(perimeter(20), 114624)
    print(perimeter(30), 14098308)
    print(perimeter(100), 6002082144827584333104)