'''
https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
'''

def sum_of_intervals(intervals):
    result = set()
    
    for interval in intervals:
        for num in range(interval[0], interval[1]):
            result.add(num)
    
    return len(result)


if __name__ == "__main__":
    print(sum_of_intervals([(1, 5)]), 4)
    print(sum_of_intervals([(1, 5), (6, 10)]), 8)
    print(sum_of_intervals([(1, 5), (1, 5)]), 4)
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)