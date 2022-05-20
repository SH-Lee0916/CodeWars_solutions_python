def permutations(string):
    result = set()
    if len(string) > 1:
        for idx in range(len(string)):
            for ch in permutations(string[0:idx] + string[idx + 1:]):
                result.add(string[idx] + ch)
    else:
        result = [string]
        
    return list(result)


# from itertools import permutations as p

# def permutations(string):
#     return [ "".join(each) for each in set(p(string, len(string))) ]


if __name__ == "__main__":
    print(permutations("a"))
    print(permutations("ab"))
    print(permutations("aabb"))