#
from c07_1_array import OwnArray

class Grid:
    def __init__(self, rows, columns, fill_value=None):
        self.data = OwnArray(rows)
        for row in range(rows):
            self.data[row] = OwnArray(columns, fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]
        
    def __str__(self):
        result =  ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result +=  str(self.data[row][col]) + " "
            result += "\n"
        return result


matrix = Grid(3, 3)
print(matrix)
for row in range(matrix.get_height()):
    for col in range(matrix.get_width()):
        matrix[row][col] =  row * col
print(matrix)
print()
print(matrix.get_height())
print(matrix.get_width())
print(matrix.__getitem__(0))
print(matrix.__getitem__(2)[2])
print(matrix.__str__())