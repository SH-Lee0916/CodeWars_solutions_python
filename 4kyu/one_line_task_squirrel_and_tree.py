'''
https://www.codewars.com/kata/59016379ee5456d8cc00000f
'''

squirrel = lambda h,H,S: round(H/h*(S*S+h*h)**.5,4)

if __name__ == "__main__":
    print(squirrel(4, 16, 3))
    print(squirrel(8, 9, 37))