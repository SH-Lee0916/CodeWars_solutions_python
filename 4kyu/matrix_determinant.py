'''
https://www.codewars.com/kata/52a382ee44408cea2500074c
'''


def determinant(matrix):
    if len(matrix) == 1:
        result = matrix[0][0]
    elif len(matrix) == 2:
        result = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        result = 0
        for idx, num in enumerate(matrix[0]):
            sub_mat = [[sub_num for c_idx, sub_num in enumerate(row) if c_idx != idx  ] for row in matrix[1:]]
            result += num * determinant(sub_mat) if (idx + 2) % 2 == 0 else -num * determinant(sub_mat)

    return result


if __name__ == "__main__":
    m1 = [ [1, 3], [2,5]]
    m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

    print(determinant([[1]]), 1, "Determinant of a 1 x 1 matrix yields the value of the one element")
    print(determinant(m1), -1, "Should return 1 * 5 - 3 * 2, i.e., -1 ")
    print(determinant(m2), -20)