'''
https://www.codewars.com/kata/585894545a8a07255e0002f1
'''

screen = {"A": set(["B", "D", "E", "F", "H"]), "B": set(["A", "C", "D", "E", "F", "G", "I"]), "C": set(["B", "D", "E", "F", "H"]),
          "D": set(["A", "B", "C", "E", "G", "H", "I"]), "E": set(["A", "B", "C", "D", "F", "G", "H", "I"]), "F": set(["A", "B", "C", "E", "G", "H", "I"]),
          "G": set(["B", "D", "E", "F", "H"]), "H": set(["A", "C", "D", "E", "F", "G", "I"]), "I": set(["B", "D", "E", "F", "H"])}

def count_patterns_from(first_point, length):
    result = set()
    stack = [first_point]
    
    while stack and length < 10 and length > 0:
        if len(stack[-1]) == length:
            result.add(stack.pop())
        else:
            pattern = stack.pop()
            cur_dot = pattern[-1]
            ## Calculate possible moving
            cur_mv = screen[cur_dot].copy()
            # Remove used, Add unused, HOW CANT I GENEALIZE IT?????
            if cur_dot == "A":
                if "B" in pattern:
                    cur_mv.add("C")
                if "D" in pattern:
                    cur_mv.add("G")
                if "E" in pattern:
                    cur_mv.add("I")
            elif cur_dot == "B":
                if "E" in pattern:
                    cur_mv.add("H")
            elif cur_dot == "C":
                if "B" in pattern:
                    cur_mv.add("A")
                if "F" in pattern:
                    cur_mv.add("I")
                if "E" in pattern:
                    cur_mv.add("G")
            elif cur_dot == "D":
                if "E" in pattern:
                    cur_mv.add("F")
            elif cur_dot == "F":
                if "E" in pattern:
                    cur_mv.add("D")
            elif cur_dot == "G":
                if "D" in pattern:
                    cur_mv.add("A")
                if "E" in pattern:
                    cur_mv.add("C")
                if "H" in pattern:
                    cur_mv.add("I")
            elif cur_dot == "H":
                if "E" in pattern:
                    cur_mv.add("B")
            elif cur_dot == "I":
                if "E" in pattern:
                    cur_mv.add("A")
                if "F" in pattern:
                    cur_mv.add("C")
                if "H" in pattern:
                    cur_mv.add("G")
            
            cur_mv = cur_mv.difference(pattern)
            for mv in sorted(cur_mv):
                stack.append(pattern + mv)
            
    return len(result)


if __name__ == "__main__":
    print(count_patterns_from('A',10), 0)
    print(count_patterns_from('A',0),  0)
    print(count_patterns_from('E',14), 0)
    print(count_patterns_from('B',1),  1)
    print(count_patterns_from('C',2),  5)
    print(count_patterns_from('E',2),  8)
    print(count_patterns_from('E',4),  256)
    
    
    # tmp = {'EDGC', 'EFBG', 'EBAH', 'EBHF', 'ECBA', 'EBGF', 'EIFD', 'ECDI', 'EHDA', 'EHIG', 'EGFB', 'EHBC', 'EABI', 'EAIB', 'EGDI', 'EAFB', 'EAIF', 'EGIH', 'EBIA', 'EDCB', 'EHDC', 'EBHD', 'EBAC', 'EHDG', 'EHFA', 'EBFC', 'EBDA', 'EAFG', 'EBCG', 'EGIC', 'EHCG', 'EBHG', 'EIDH', 'EGCD', 'EAHB', 'EIAH', 'EFAB', 'EDHG', 'EGIA', 'ECHA', 'EAHI', 'ECFH', 'EHIF', 'EGCI', 'EHFG', 'EHBA', 'EGDB', 'EIFH', 'EIBD', 'EDFB', 'ECBF', 'EHGD', 'EFIG', 'EDFH', 'EBFA', 'EGCF', 'ECDF', 'EABC', 'EFDH', 'EDAI', 'EGFD', 'EBGH', 'ECHG', 'EFHC', 'EFBH', 'EGBA', 'EBAF', 'EDFA', 'EDAG', 'EDGH', 'EBIH', 'EFGC', 'EBAD', 'EIDB', 'ECHB', 'EFCG', 'EGIB', 'EBCI', 'EHCD', 'EDHF', 'EDBH', 'EGCA', 'EIDG', 'EDGI', 'EHAI', 'EGBH', 'ECFD', 'EDCI', 'EGHD', 'ECHD', 'EHFI', 'EABF', 'EDCH', 'EHAD', 'EDHB', 'EDGB', 'EIHC', 'EHDF', 'EDFC', 'EHAF', 'EBCF', 'ECDG', 'EAHG', 'EABH', 'EDBI', 'EBCA', 'EGCB', 'EFGH', 'EGAD', 'EDIG', 'EIFC', 'ECFI', 'EFIC', 'EDAF', 'EGHI', 'EAID', 'EDGF', 'EBDC', 'EBDH', 'EBFH', 'EBGI', 'EDIH', 'EFIB', 'EBDF', 'EGBD', 'EHGI', 'EDHI', 'EIDA', 'EDIA', 'EBGC', 'EGDA', 'EHCB', 'EFGD', 'EIHB', 'EGAC', 'EGID', 'EFBC', 'EGBC', 'EFIA', 'EHCF', 'EBCD', 'EABG', 'ECBH', 'EDHC', 'EHID', 'EDBC', 'EFHA', 'ECGF', 'EBIC', 'EFBA', 'ECDA', 'EHFD', 'ECBI', 'ECBG', 'EDFG', 'EFDB', 'EBDI', 'EFDI', 'EIBG', 'EAHC', 'EGAI', 'EGAH', 'EBHI', 'EGCH', 'EGDF', 'EAIH', 'ECFA', 'EDCF', 'EDGA', 'EADF', 'ECFG', 'EHIA', 'EHGC', 'EAFI', 'EBGA', 'EGDH', 'EIFA', 'EGFH', 'EBHA', 'EHAB', 'ECFB', 'ECHF', 'EIBF', 'EFDG', 'EIHF', 'EAFH', 'EHFC', 'EHFB', 'EDHA', 'EDFI', 'EHDI', 'EBHC', 'EGHC', 'EADH', 'EFCI', 'EDCG', 'EIAB', 'EFBI', 'EFDC', 'EAFD', 'EBFI', 'EAHF', 'EFHB', 'EADC', 'ECDH', 'EGIF', 'EFHG', 'EFHI', 'EIHG', 'ECDB', 'EDBF', 'ECHI', 'EBGD', 'EHDB', 'EFID', 'EDAB', 'EBIG', 'EFCH', 'EGBF', 'EIDC', 'EFBD', 'EGDC', 'EIBC', 'EIBH', 'EBIF', 'EIHA', 'EHBG', 'EIAF', 'EGFA', 'EBAG', 'EGFC', 'EHBF', 'EIFG', 'EDIB', 'EHBI', 'EFCD', 'EFHD', 'EDBA', 'EADI', 'EGAF', 'EGHB', 'ECGB', 'EIHD', 'EBFD', 'EDIF', 'ECGD', 'EABD', 'EDAH', 'EHGF', 'EBID', 'EGBI', 'EIAD', 'EBCH', 'EGHF', 'EFDA', 'EFAH', 'EGHA', 'EBDG', 'EIFB', 'EADB', 'EAFC', 'EGAB', 'EADG', 'EIBA', 'EHIB', 'EAHD', 'EIDF', 'EFGB', 'EBAI', 'EBFG', 'ECGH', 'EHBD', 'EHGB', 'EFAI', 'EFGI', 'EDIC', 'EFAD', 'ECBD', 'EFIH', 'EFCB', 'EGFI', 'EDBG'}
    # tmp1 = {'EDGF', 'EHFB', 'EDBH', 'EGDB', 'EBHG', 'EDIH', 'EGBC', 'EFHG', 'EBDA', 'EBGH', 'EGAI', 'EFCA', 'EFBD', 'ECGB', 'EFAH', 'EDHI', 'EHID', 'EBAC', 'EFIH', 'EHGB', 'ECFI', 'EDAF', 'EGFI', 'EFIG', 'EFCB', 'EFIC', 'ECBA', 'EBAD', 'EAFC', 'EDIA', 'EBGD', 'EGHC', 'EHDI', 'EBCH', 'EBIH', 'EGCD', 'EHAF', 'EFIB', 'EDHG', 'ECGI', 'ECHF', 'EIHD', 'EGFD', 'EBAI', 'EDGA', 'ECFA', 'EACD', 'EAGI', 'EBCF', 'EHAD', 'EBFG', 'EAFH', 'EHCB', 'EBCA', 'EBFA', 'EDCB', 'EAIC', 'EHIA', 'EADH', 'EFHC', 'ECDF', 'EGDF', 'EACB', 'EGFH', 'EACG', 'EFCI', 'EGHF', 'EFAD', 'ECDG', 'EGBH', 'EFDI', 'EHGD', 'ECBG', 'EFHB', 'EDFB', 'EDAI', 'EFGC', 'EFCD', 'EAGF', 'EADI', 'EFBC', 'EBIG', 'EHCG', 'EAIG', 'EGDH', 'EGHA', 'EAGC', 'EGIB', 'EHDC', 'EBFI', 'EADF', 'EGAB', 'EFDC', 'EBDH', 'EFAI', 'EIHA', 'ECHI', 'EAIB', 'EADB', 'EFIA', 'EFGH', 'EDCF', 'ECBD', 'EBAF', 'EFDA', 'EAFG', 'EDBF', 'EDBI', 'ECGF', 'EGFA', 'EGCH', 'EGDA', 'EGBD', 'EDHB', 'EDHA', 'EBHA', 'EHAI', 'EFBG', 'EBGA', 'EAFD', 'EIFD', 'EDFH', 'EDFG', 'EBGF', 'ECHG', 'EFCH', 'EABC', 'EHIG', 'EGID', 'ECHA', 'EIDB', 'EIBA', 'EIBG', 'ECBH', 'ECGD', 'EBGI', 'EGCF', 'EGAC', 'EBGC', 'EFHA', 'EABG', 'EHBG', 'EABF', 'EDHC', 'EIAF', 'EBHI', 'EGFB', 'EFHD', 'EHDA', 'EAGD', 'EAHD', 'EIBC', 'EDFI', 'EFDB', 'EIDH', 'EBFC', 'EHBF', 'EIBH', 'EBFD', 'EHDB', 'ECDA', 'EGDI', 'EIFH', 'EGBI', 'EHGC', 'EDGB', 'EHCD', 'ECGH', 'EGAD', 'ECFG', 'EBHF', 'EBAH', 'EFGA', 'EAHC', 'EAGB', 'EHFD', 'EBIA', 'EHAB', 'EGHB', 'EFDH', 'EIHC', 'EAHB', 'EHGI', 'ECDI', 'EADG', 'EGAH', 'EIHG', 'EIHB', 'EDAH', 'EBCG', 'EFGI', 'EIFG', 'EGHI', 'EHAG', 'EFGB', 'EIAB', 'EGCB', 'EBHD', 'EFAC', 'EAFB', 'EHFI', 'EDIB', 'EGBA', 'EGBF', 'EFCG', 'EFAG', 'EADC', 'EFBA', 'EAHI', 'EABI', 'EIFC', 'EIDF', 'EIDA', 'EAGH', 'EIFB', 'EDAB', 'EGIA', 'EAHG', 'EABH', 'EGDC', 'EFGD', 'EDFA', 'EDCH', 'EIAD', 'EFBH', 'EAID', 'EAFI', 'EHDG', 'EDIF', 'EDGH', 'ECBI', 'EHFA', 'EIFA', 'EDHF', 'ECDB', 'EBCD', 'EDFC', 'EIBD', 'EBDG', 'EGHD', 'EBFH', 'EIBF', 'EFBI', 'EACI', 'EHFG', 'ECHD', 'EBAG', 'EBHC', 'EBID', 'EHGF', 'EHBI', 'EIAH', 'EHIB', 'ECGA', 'EAIF', 'EFDG', 'EAIH', 'EIDG', 'ECFD', 'EFID', 'EFHI', 'EFAB', 'EDBC', 'EHBD', 'ECDH', 'EDGC', 'EGIH', 'EGCA', 'EAHF', 'ECBF', 'EHFC', 'EGFC', 'ECHB', 'EDBG', 'EDBA', 'EIDC', 'EHBC', 'ECFB', 'EBIF', 'EBDF', 'EHIF', 'EACF', 'EHDF', 'EDCG', 'EACH', 'EABD', 'EGIF', 'EGAF', 'EHGA', 'EDAG', 'ECFH', 'EBDI', 'EIHF', 'EBDC', 'EHCF', 'EHBA'}
    
    # print(tmp1 - tmp)