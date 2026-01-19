# Игра далеко не оконченная, сделано строго под ТЗ задачи
# Ссылка на задачу Stepik -> https://stepik.org/lesson/701992/step/10?unit=702093

from random import randint

class BooleanDesc:
    def __set_name__(self, owner_cls, name: str):
        self.name = '__' + name
        
    def __get__(self, instance, owner_cls) -> bool:
        if instance is None:
            return property()
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value: bool):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        instance.__dict__[self.name] = value
        

class Cell:
    is_mine, is_open = BooleanDesc(), BooleanDesc()
    
    def __init__(self):
        self.is_mine, self.is_open = False, False
        self.__number = 0
        
    @property
    def number(self) -> int:
        return self.__number
    
    @number.setter
    def number(self, value: int):
        if not (type(value) is int and 0 <= value <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value
        
    def __bool__(self) -> bool: #закрыта ли ячейка
        return not self.is_open

    
class GamePole:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def __init__(self, N: int, M: int, total_mines: int):
        self.rows, self.cols, self.total_mines = N, M, total_mines
    
    def init_pole(self):
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.cols)) for _ in range(self.rows))
        self.place_on_mines(self.rows, self.cols, self.total_mines)

    def place_on_mines(self, N: int, M: int, total_mines: int):
        while total_mines:
            row, col = randint(0, N - 1), randint(0, M - 1)
            if self.__pole_cells[row][col]:
                self.open_cell(row, col)
                self.__pole_cells[row][col].is_mine = True
                total_mines -= 1
                for i in range(max(row - 1, 0), min(row + 2, self.rows)):
                    for j in range(max(col - 1, 0), min(col + 2, self.cols)):
                        self.open_cell(i, j)
                        self.__pole_cells[i][j].number += 1
                    
    def open_cell(self, i: int, j: int):
        if not (type(i) == type(j) == int and 0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True
        
    @property
    def pole(self) -> tuple[tuple[int, ...], ...]:
        return self.__pole_cells
    
    def show_pole(self):
        for row in self.pole:
            for cell in row:
                print('#' if cell else ('*' if cell.is_mine else cell.number), end = ' ')
            print()




#Tests:

# p1 = GamePole(10, 20, 10)
# p2 = GamePole(10, 20, 10)
# assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
# p = p1

# cell = Cell()
# assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

# cell.is_mine = True
# cell.number = 5
# cell.is_open = True
# assert bool(cell) == False, "функция bool() вернула неверное значение"

# try:
#     cell.is_mine = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"

    
# try:
#     cell.number = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"

# p.init_pole()
# m = 0
# for row in p.pole:
#     for x in row:
#         assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
#         if x.is_mine:
#             m += 1

# assert m == 10, "на поле расставлено неверное количество мин"
# p.open_cell(0, 1)
# p.open_cell(9, 19)

# try:
#     p.open_cell(10, 20)
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"


# def count_mines(pole, i, j):
#     n = 0
#     for k in range(-1, 2):
#         for l in range(-1, 2):
#             ii, jj = k+i, l+j
#             if ii < 0 or ii > 9 or jj < 0 or jj > 19:
#                 continue
#             if pole[ii][jj].is_mine:
#                 n += 1
                
#     return n


# for i, row in enumerate(p.pole):
#     for j, x in enumerate(row):
#         if not p.pole[i][j].is_mine:
#             m = count_mines(p.pole, i, j)
#             assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
