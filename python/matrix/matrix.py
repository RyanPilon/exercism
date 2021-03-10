class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in index.split()]for index in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [col[index - 1] for col in self.matrix]
