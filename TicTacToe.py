#Тесты немного нелогичные, одна сторона ходит 3 раза подряд. Получается выиграть можно и за меньшее кол-во ходов чем 5)

from random import randint

class Cell:
    def __init__(self, value: int=0):
        self.value = value
       
    def __bool__(self) -> bool:
        return not self.value
    
    
class TicTacToe:
    FREE_CELL = 0 # свободная клетка
    HUMAN_X = 1 # крестик (игрок - человек)
    COMPUTER_O = 2 # нолик (игрок - компьютер)
    winner = ''
    
    def init(self):
        self.__init__()
    
    def __init__(self):
        self.pole = tuple(tuple(Cell(self.FREE_CELL) for _ in range(3)) for _ in range(3))
        self.winner, self.moves = '', 0
        
    def __getitem__(self, indexes: tuple[int, int]) -> int:
        row, col = indexes
        if not (type(row) == type(col) == int and 0 <= row <= 2 and 0 <= col <= 2):
            raise IndexError('некорректно указанные индексы')
        return self.pole[row][col].value
    
    def __setitem__(self, indexes: tuple[int, int], value: int) -> int:
        row, col = indexes
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise IndexError('некорректно указанные индексы')
        if self.pole[row][col].value:
            raise ValueError('данная ячейка занята')
        
        self.pole[row][col].value = value
        self.moves += 1
        self.check_game_status()
        
    def show(self):
        for row in self.pole:
            print(*map(lambda x: x.value, row))
    
    def human_go(self):
        while True:
            row, col = input("Введите строку"), input("Введите колонку")
            if row.isdigit() and col.isdigit() and 0 <= int(row) <= 2 and 0 <= int(col) <= 2:
                row, col = int(row), int(col)
                break
        
        self[row, col] = TicTacToe.HUMAN_X
        
    def computer_go(self):
        while True:
            row, col = randint(0, 2), randint(0, 2)
            if self[row, col] == self.FREE_CELL:
                self[row, col] = TicTacToe.COMPUTER_O
                break
    
    @property
    def is_human_win(self) -> bool:
        return self.winner == 'human'
    
    @property
    def is_computer_win(self) -> bool:
        return self.winner == 'computer'
    
    @property
    def is_draw(self) -> bool:
        return self.winner == 'draw'
    
    def __bool__(self) -> bool:
        return not self.winner
    
    def check_game_status(self):
        #if self.moves < 5:
         #   return
        
        if not any(cell.value == 0 for row in self.pole for cell in row):
            self.winner = 'draw'
            return
        
        for a, b, c in (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                       ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                       ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))):
            
            elems = (self.pole[a[0]][a[1]].value, self.pole[b[0]][b[1]].value, self.pole[c[0]][c[1]].value)
            if elems == (self.HUMAN_X, ) * 3:
                self.winner = 'human'
            elif elems == (self.COMPUTER_O, ) * 3:
                self.winner = 'computer' 
            
            if self.winner: return




#Tests:
cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
# assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
# cell.value = 1
# assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

# assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

# game = TicTacToe()
# assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
# assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
# game[1, 1] = TicTacToe.HUMAN_X
# assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

# game[0, 0] = TicTacToe.COMPUTER_O
# assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

# game.init()
# assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

# try:
#     game[3, 0] = 4
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"

# game.init()
# assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

# game[0, 0] = TicTacToe.HUMAN_X
# game[1, 1] = TicTacToe.HUMAN_X
# game[2, 2] = TicTacToe.HUMAN_X

# assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

# game.init()
# game[0, 0] = TicTacToe.COMPUTER_O
# game[1, 0] = TicTacToe.COMPUTER_O
# game[2, 0] = TicTacToe.COMPUTER_O
# assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
