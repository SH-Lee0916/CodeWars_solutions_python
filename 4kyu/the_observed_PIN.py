'''
https://www.codewars.com/kata/5263c6999e0f40dee200059d
'''

from itertools import product


def get_pins(observed):
    possible_nums = []
    for num in observed:
        tmp_num = num
        if num == "0":
            tmp_num += "8"
        else:
            # horizental
            hor_check = int(num) % 3
            if hor_check == 1:
                tmp_num += str(int(num) + 1)
            elif hor_check == 2:
                tmp_num += str(int(num) + 1)
                tmp_num += str(int(num) - 1)
            elif hor_check == 0:
                tmp_num += str(int(num) - 1)
            
            # vertical
            ver_check = (int(num) - 1) // 3
            if ver_check == 0:
                tmp_num += str(int(num) + 3)
            elif ver_check == 1:
                tmp_num += str(int(num) + 3)
                tmp_num += str(int(num) - 3)
            elif ver_check == 2:
                tmp_num += str(int(num) - 3)
                if hor_check == 2:
                    tmp_num += "0"
            
            
        possible_nums.append(tmp_num)
    
    possible_pins = [ "".join(nums) for nums in list(product(*possible_nums)) ]
    
    return possible_pins