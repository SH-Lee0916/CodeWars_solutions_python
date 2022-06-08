'''
https://www.codewars.com/kata/525c65e51bf619685c000059/
'''

def cakes(recipe, available):
    cakes_num = 999999999
    
    for igdt in recipe.keys():
        if igdt in available.keys():
            cakes_num = min(cakes_num, available[igdt] // recipe[igdt])
        else:
            cakes_num = 0
           
    return cakes_num


if __name__ == "__main__":
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available), 2, 'example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe, available), 0, 'example #2')