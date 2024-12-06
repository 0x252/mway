from abc import ABC,abstractmethod
import random
class Animal(ABC):
    def __init__(self):
        self._who = "randomAnimal"
    @abstractmethod
    def voice(s):
        pass
    @property
    def who(self):
        return self._who
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, v):
        if v >= 0: self._age = v
        else: raise ValueError("Age will be more than 0")
    #def getAge(self): return self.age
    def setAge(self, age):
        self._age = age
    def __init__(self, age=0):
        self._age = age
        print("Init animal")

class Dog(Animal):
    def __init__(self):
        #super(Animal)
        self._who = "Dog"
        print("Dog init")
        super().__init__()
    def voice(self):
        print("Woof")

class Cat(Animal):
    def __init__(self):
        self._who = "Cat"
    def voice(self):
        print("Meow")

class Bulldog(Dog):
    def someAnAnotherLogic(self):
        print("logic")


if __name__ == '__main__':
    mBullDog = Bulldog()
    mDog = Dog()
    mCat = Cat()
    mCat.age = 1
    mDog.age = 2
    animals = [mBullDog, mDog, mCat]
    for animal in animals:
        animal.voice()
        print(f'Animal: {animal.who} {animal.age}')
        if isinstance(animal,Bulldog):
            animal.someAnAnotherLogic()
    try:
     mBullDog.age = -1
    except Exception as e:
        print(f'error: {e}')
    
