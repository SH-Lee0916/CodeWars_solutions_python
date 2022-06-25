'''
https://www.codewars.com/kata/5902bc7aba39542b4a00003d
'''

food_chain = {
    "antelope": ("grass"),
    "big-fish": ("little-fish"),
    "bug": ("leaves"),
    "bear": ("big-fish", "bug", "chicken", "cow", "leaves", "sheep"),
    "chicken": ("bug"),
    "cow": ("grass"),
    "fox": ("chicken", "sheep"),
    "giraffe": ("leaves"),
    "lion": ("antelope", "cow"),
    "panda": ("leaves"),
    "sheep": ("grass")
}

def who_eats_who(zoo):
    result = [zoo]
    animals = zoo.split(",")
    
    animal_idx = 0
    while animal_idx < len(animals):
        # check left and re-arrange idx
        while animal_idx > 0 and animals[animal_idx - 1] in food_chain.get(animals[animal_idx], ()):
            result.append(f"{animals[animal_idx]} eats {animals.pop(animal_idx - 1)}")
            animal_idx -= 2
        
        # check right
        while animal_idx >= 0 and animal_idx < len(animals) - 1 and animals[animal_idx + 1] in food_chain.get(animals[animal_idx], ()):
            result.append(f"{animals[animal_idx]} eats {animals.pop(animal_idx + 1)}")
            
        animal_idx += 1
        
    result.append(f"{','.join(animals)}")
    
    return result


if __name__ == "__main__":
    input = "fox,bug,chicken,grass,sheep"
    expected = ["fox,bug,chicken,grass,sheep", 
                "chicken eats bug", 
                "fox eats chicken", 
                "sheep eats grass", 
                "fox eats sheep", 
                "fox"]
    print(who_eats_who(input), expected)