'''
https://www.codewars.com/kata/5672682212c8ecf83e000050

'''

def dbl_linear(n):
    u = [1]
    
    y_idx, z_idx = 0, 0
    
    for idx in range(n):
        y = 2 * u[y_idx] + 1
        z = 3 * u[z_idx] + 1
        if y < z:
            u.append(y)
            y_idx += 1
        elif y > z:
            u.append(z)
            z_idx += 1
        elif y == z:
            u.append(y)
            y_idx += 1
            z_idx += 1
    
    return u[n]