'''
https://www.codewars.com/kata/51b66044bce5799a7f000003
'''

roman2num = { "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD":400, "D": 500, "CM": 900, "M": 1000 }
num2roman = { v: k for k, v in roman2num.items() }

class RomanNumerals:
    def num2ro(val, num):
        if val < 4:
            result = f"{num2roman[num] * val}"
        elif val == 4:
            result = f"{num2roman[num * 4]}"
        elif val >= 5 and val < 9:
            result = f"{num2roman[num * 5] + (num2roman[num] * (val - 5))}"
        elif val == 9:
            result = f"{num2roman[num * 9]}"
        return result


    def to_roman(val):
        result = ""

        thousand, rem = divmod(val, 1000)
        hundred, rem = divmod(rem, 100)
        ten, one = divmod(rem, 10)

        result += f"{num2roman[1000] * thousand}"
        result += RomanNumerals.num2ro(hundred, 100)
        result += RomanNumerals.num2ro(ten, 10)
        result += RomanNumerals.num2ro(one, 1)

        return result


    def from_roman(roman_num):
        nums = [roman2num[roman_num[0]]]
        for ch in roman_num[1:]:
            if nums[-1] < roman2num[ch]:
                nums.append(roman2num[ch] - nums.pop())
            else:
                nums.append(roman2num[ch])

        return sum(nums)


if __name__ == "__main__":
    print("to_roman")
    print(RomanNumerals.to_roman(1000), 'M')
    print(RomanNumerals.to_roman(4), 'IV')
    print(RomanNumerals.to_roman(1), 'I')
    print(RomanNumerals.to_roman(1990), 'MCMXC')
    print(RomanNumerals.to_roman(2008), 'MMVIII')
    print('from_roman')
    print(RomanNumerals.from_roman('XXI'), 21)
    print(RomanNumerals.from_roman('I'), 1)
    print(RomanNumerals.from_roman('IV'), 4)
    print(RomanNumerals.from_roman('MMVIII'), 2008)
    print(RomanNumerals.from_roman('MDCLXVI'), 1666)