'''
https://www.codewars.com/kata/5629db57620258aa9d000014
'''
from collections import Counter


def mix(s1, s2):
    result = []
    s1_cnt = { key:value for key, value in Counter(s1).items() if key.isalpha() and value > 1 and key.islower()}
    s2_cnt = { key:value for key, value in Counter(s2).items() if key.isalpha() and value > 1 and key.islower() }
    common_ch = { key for key in s1_cnt.keys() if key in s2_cnt.keys() }
    
    # Common
    for ch in common_ch:
        if s1_cnt[ch] > s2_cnt[ch]:
            result.append(f"1:{ch * s1_cnt[ch]}")
        elif s1_cnt[ch] < s2_cnt[ch]:
            result.append(f"2:{ch * s2_cnt[ch]}")
        elif s1_cnt[ch] == s2_cnt[ch]:
            result.append(f"=:{ch * s1_cnt[ch]}")
    
    # rest of s1
    for key in s1_cnt.keys() - common_ch:
        result.append(f"1:{key * s1_cnt[key]}")
    
    # rest of s2
    for key in s2_cnt.keys() - common_ch:
        result.append(f"2:{key * s2_cnt[key]}")
        
    result.sort(key = lambda x: (-len(x.split(":")[-1]), x.split(":")[0], x.split(":")[-1][0]))
    
    return "/".join(result)


if __name__ == "__main__":
    print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
    print(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
    print(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
    print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
    print(mix("codewars", "codewars"), "")
    print(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")