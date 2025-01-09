'''class Example:
    houses_history = [1]

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return super().__new__(cls)

    def __init__(self, one, two, thri):
        print(one)
        print(two)
        print(thri)

ex = Example('data', two=25, thri=3.14)
print(Example.houses_history)'''

class House():
    houses_history = []

    def __new__(cls, *args):
        #print(args)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors
        House.houses_history.append(self.name)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("Такого этажа не существует",'\n')
        else:
            for i in range(1, new_floor + 1):
                print(i)
            print("Приехали",'\n')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __len__(self):
        return self.floors

    def __eq__(self, other):
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors == other.floors
        return False

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other) #такое решение, а если много параметров?
        return False

    def __iadd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        return False

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        return False

    def __gt__(self, other):#(>)
        if isinstance(other, int):
            return self.floors > other.floors
        return False

    def __ge__(self, other):#(>=)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors >= other.floors
        return False

    def __lt__(self, other):#(<)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors < other.floors
        return False

    def __le__(self, other): #(<=)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors <= other.floors
        return False

    def __ne__(self, other): #(!=)
        if isinstance(other, House) and isinstance(other.floors,int):
            return self.floors != other.floors
        return False

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(h1)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
