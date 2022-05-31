'''
https://www.codewars.com/kata/598106cb34e205e074000031
'''

def count_deaf_rats(town):
    rats = town.split("P")
    rats[0] = rats[0].replace(" ", "")
    rats[1] = rats[1].replace(" ", "")
    
    deaf_rats = 0
    for idx in range(0, len(rats[0]), 2):
        if rats[0][idx:idx + 2] == "O~":
            deaf_rats += 1
    
    for idx in range(0, len(rats[1]), 2):
        if rats[1][idx:idx + 2] == "~O":
            deaf_rats += 1
            
    return deaf_rats
    

if __name__ == "__main__":
    print(count_deaf_rats("~O~O~O~O P"), 0)
    print(count_deaf_rats("P O~ O~ ~O O~"), 1)
    print(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)