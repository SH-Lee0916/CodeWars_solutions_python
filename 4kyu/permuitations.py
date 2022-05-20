from itertools import permutations as p

def permutations(string):
    return [ "".join(each) for each in set(p(string, len(string))) ]


if __name__ == "__main__":
    print(permutations("a"))
    print(permutations("ab"))
    print(permutations("aabb"))