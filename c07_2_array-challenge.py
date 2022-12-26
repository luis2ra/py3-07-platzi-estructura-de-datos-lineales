# Challenge

'''
1. Crear una clase array.
2. Incorpora un metodo para poblar sus slots con numeros aleatorios o secuenciales.
3. Incluye un metodo que sume todos los valores del array

'''
from random import randrange

class DemoArray:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def llenar(self):
        for i in range(self.__len__()):
            print(i)
            self.__setitem__(i, randrange(1, 10))

    def sumar(self):
        i = 0
        suma = 0
        while i < self.__len__():
            suma += self.__getitem__(i)
            i += 1
        return suma

array1 =  DemoArray(5)
print(array1)
array1.llenar()
print(array1)
print(array1.sumar())
print('the end...')
