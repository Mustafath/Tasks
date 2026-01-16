#Lite (not full) version if singly linked list
#Link to task -> https://stepik.org/lesson/701994/step/10?unit=70209



class StackObj:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None
        
    
class Stack:
    def __init__(self) -> None:
        self.top = self.tail = None
        self.length = 0
        self.iteration_obj = self.top # атрибут для хранения следующего элемента возвращаемого с __next__ (изначально первый элемент)
        
    def check_index(self, index: int) -> None:
        ''' Проверка индекса на корректность (тип и принадлежность к диапазону [0:stack.length)) '''
        if not (type(index) is int and 0 <= index < self.length):
            raise IndexError('неверный индекс')
        
    def get_by_index(self, index: int) -> StackObj:
        ''' Возвращает элемент стека по индексу '''
        item, position = self.top, 0
        while position != index:
            item = item.next
            position += 1    
        return item
        
    def push_front(self, item: StackObj) -> None:
        '''Добавляет элемент в начало стека'''
        if self.length == 0:
            self.top = self.tail = item
        else:
            item.next = self.top
            self.top = item
        self.length += 1

    def push_back(self, item: StackObj) -> None:
        '''Добавляет элемент в конец стека'''
        if self.length == 0:
            self.top = self.tail = item
            
        else:
            self.tail.next = item
            self.tail = item
        self.length += 1 
           
    def __getitem__(self, index: int) -> str:
        ''' Возвращает значение атрибута data у элемента(StackObj) в стеке по индексу '''
        self.check_index(index) # проверка индекса на корректность
        
        item = self.get_by_index(index)
        return item.data
    
    def __setitem__(self, index: int, data: str) -> None:
        ''' Меняет значение атрибута data у элемента(StackObj) в стеке по индексу '''
        self.check_index(index) # проверка индекса на корректность
        
        item = self.get_by_index(index)
        item.data = data
        
    def __len__(self) -> int:
        return self.length
    
    def __iter__(self) -> "Stack":
        self.iteration_obj = self.top
        return self
    
    def __next__(self) -> StackObj:
        if self.iteration_obj is None:
            raise StopIteration
        elem = self.iteration_obj
        self.iteration_obj = self.iteration_obj.next
        return elem
