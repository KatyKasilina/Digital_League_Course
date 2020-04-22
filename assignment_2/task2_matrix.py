## 2) Реализуйте класс Matrix (математический концепт "квадратной матрицы").
##(должны быть реализованы основные операции: сложение, умножение, транспонирование)

from copy import deepcopy


class Matrix:
    def __init__(self, lst):
        self.matrix = deepcopy(lst)
        self.dim_row = len(self.matrix)
        self.dim_col = len(self.matrix[0])

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for row in self.matrix:
                row_list = []
                for element in row:
                    row_list.append(element*other)
                result.append(row_list)
            return Matrix(result)
        elif self.dim_col != other.dim_row:
            return 'Matrices cannot be multiplied!'
        else:
            main_rows = range(self.dim_row)
            main_cols = range(self.dim_col)
            other_cols = range(other.dim_col)
            result = []
            for mr in main_rows:
                res = []
                for oc in other_cols:
                    mu, summ = 0, 0
                    for mc in main_cols:
                        mu = self.matrix[mr][mc] * other[mc][oc]
                        summ += mu
                    res.append(summ)
                result.append(res)
            return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if self.dim_row == other.dim_row and self.dim_col == other.dim_col:
            result = []
            for r in range(self.dim_row):
                res = []
                for c in range(self.dim_col):
                    summ = self.matrix[r][c] + other[r][c]
                    res.append(summ)
                result.append(res)
            return Matrix(result)
        else:
            print('Matrices cannot be added!')

    def transpose(self):
        result = list(map(list, zip(*self.matrix)))
        return Matrix(result)

## 3) Напишите реализацию метода Гаусса-Жордана для нахождения обратной матрицы, работающий с классом Matrix.

