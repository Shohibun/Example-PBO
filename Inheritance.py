#INHERITANCE
class Animal(object):
    def __init__(self, name):
        self.name = name 

    def Eat(self, food):
        print('%s is eating %s. ' %(self.name, food))

class Dog(Animal):
    def Fetch(self, thing):
        print('%s goes after the %s!' %(self.name, thing))

class Cat(Animal):
    def SwatString(self):
        print('%s shreads the stirng!' %(self.name))

D = Dog('Ranger')
C = Cat('Meow')

D.Fetch('Ball')
C.SwatString()
D.Eat('Dog food')
C.Eat('Cat food')
