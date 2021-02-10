from typing import List

class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])

    def __add__(self, other):
        result = []
        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)

matrix1 = Matrix([[41, 42, 21], [13, 14, 22], [13, 14, 22]])
print(matrix1, '\n')
matrix2 = Matrix([[10, 20, 44], [30, 40, 55], [13, 14, 22]])
print(matrix2, '\n')
print(matrix1 + matrix2)
