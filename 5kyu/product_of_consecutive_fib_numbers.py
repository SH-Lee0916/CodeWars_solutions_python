'''
https://www.codewars.com/kata/5541f58a944b85ce6d00006a/
'''

def productFib(prod):
    fib = [0, 1]
    
    while fib[-2] * fib[-1] < prod:
        fib.append(fib[-2] + fib[-1])
    
    return [fib[-2], fib[-1], (fib[-2] * fib[-1]) == prod]


if __name__ == "__main__":
    print(productFib(4895), [55, 89, True])
    print(productFib(5895), [89, 144, False])
