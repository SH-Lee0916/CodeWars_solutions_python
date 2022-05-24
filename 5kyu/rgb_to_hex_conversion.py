'''
https://www.codewars.com/kata/513e08acc600c94f01000001
'''

def check_range(value):
    if value < 0:
        value = 0
    elif value > 255:
        value = 255
    return value

def rgb(r, g, b):
    r = check_range(r)
    g = check_range(g)
    b = check_range(b)
    return f"{r:02x}{g:02x}{b:02x}".upper()


if __name__ == "__main__":
    print(rgb(0,0,0),"000000", "testing zero values")
    print(rgb(1,2,3),"010203", "testing near zero values")
    print(rgb(255,255,255), "FFFFFF", "testing max values")
    print(rgb(254,253,252), "FEFDFC", "testing near max values")
    print(rgb(-20,275,125), "00FF7D", "testing out of range values")