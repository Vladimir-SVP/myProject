class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors        
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return print('Ошибка')
    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return print('Ошибка')        
    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
           return self.number_of_floors <= other.number_of_floors
        else:
            return print('Ошибка')        
    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
           return self.number_of_floors > other.number_of_floors
        else:
            return print('Ошибка')
    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
           return self.number_of_floors >= other.number_of_floors
        else:
            return print('Ошибка')
    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
           return self.number_of_floors != other.number_of_floors
        else:
            return print('Ошибка')
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return print('Ошибка')        
    def __iadd__(self, value):
        return self.__add__(value)
        # if isinstance(value, int):
        #     self.number_of_floors = self.number_of_floors + value
        #     return self
        # else:
        #     return print('Ошибка')
    def __radd__(self, value):
        return self.__add__(value)
        # if isinstance(value, int):
        #     self.number_of_floors = self.number_of_floors + value
        #     return self
        # else:
        #     return print('Ошибка')    
        
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__