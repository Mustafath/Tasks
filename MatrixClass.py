# Link to Stepik task -> https://stepik.org/lesson/701994/step/12?unit=702095 
# Реализация класса Matrix для операций с матрицами (неполноценная, сделано под ТЗ)


from typing import Self, Callable
from operator import add as operator_add, sub as operator_sub

class Matrix:
    def __init__(self, *args):
        if len(args) == 1: # если передана готовая матрица (двумерный список)
            matrix = args[0]
            if not all(len(row) == len(matrix[0]) and all(type(cell) in (int, float) for cell in row)
                   for row in matrix): # проверка на прямоугольность матрицы и тип значений ячеек (только числа)  
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.matrix = matrix
        
        elif len(args) == 3: # если переданы данные для создания новой матрицы
            rows, cols, fill_value = args[0], args[1], args[2]
            if tuple(map(type, (rows, cols))) != (int, int) or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.matrix = [[fill_value for _ in range(cols)] for _ in range(rows)]
    
    
    def check_indexes(self, row: int, col: int):
        rows, cols = len(self.matrix), len(self.matrix[0])
        if not all(type(index) is int and 0 <= index < mx 
                   for index, mx in ((row, rows), (col, cols))): 
            raise IndexError('недопустимые значения индексов')
    
    def __getitem__(self, indexes: tuple[int, int]) -> int | float:
        row, col = indexes
        self.check_indexes(row, col)
        return self.matrix[row][col]
    
    def __setitem__(self, indexes: tuple[int, int], value: int | float):
        row, col = indexes
        self.check_indexes(row, col)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.matrix[row][col] = value
        
    @staticmethod
    def calculate(matrix1: Self, operand: Self | int | float,
                  operator: Callable[[int | float, int | float], int | float]) -> Self: 
        ''' Функция для создания новой матрицы на основе существующей матрицы и второго операнда, данные 
        которых будут зависеть еще от переданного мат.оператора - operator. 
        Возможные операции: 
        1) сложение соответствующих значений элементов матриц matrix1 и operand;
        2) вычитание соответствующих значений элементов матриц matrix1 и operand
        3) прибавление числа operand ко всем элементам матрицы matrix1
        4) вычитание числа operand из всех элементов матрицы matrix1'''
        matrix1 = matrix1.matrix # для работы с непосредственно самой матрицей
        
        if type(operand) in (float, int): # если операнд число
            return Matrix([[operator(cell, operand) for cell in row] for row in matrix1])
        
        if isinstance(operand, Matrix) and (len(matrix1), len(matrix1[0])) == (len(operand.matrix), len(operand.matrix[0])): # если операнд матрица равных размеров
            return Matrix([[operator(matrix1[i][j], operand.matrix[i][j]) for j in range(len(operand.matrix[0]))]
                       for i in range(len(operand.matrix))])
        
        raise ValueError('операции возможны только с матрицами равных размеров')
        
    def __add__(self, other: Self | int | float) -> Self:
        return self.calculate(self, other, operator_add)
    
    def __sub__(self, other: Self | int | float) -> Self:
        return self.calculate(self, other, operator_sub)
