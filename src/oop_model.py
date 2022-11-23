# covariance call
from typing import List

class Dog:
    ...

class DogContainer:

    def __init__(self, dogs: List[Dog]):
        self.dogs = dogs

class Corgi(Dog):
    ...

corgis: List[Corgi] = [Corgi(), Corgi()]
container = DogContainer(dogs=corgis)

# Здесь ошибка так как класс ковариантен

# polymorhic call

class DogPhotographer:

    def __init__(self, dogs: List[Dog]):
        self.dogs = dogs

photgrapher = DogPhotographer(dogs=corgis)

# здесь работает инициализация, так идет полиморфная обработка корги как потомков собак