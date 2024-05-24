class Animal(object):
    def run(self):
        print("Animal is runing...")


class Dog(Animal):
    def run(self):
        print("Dog is runing...")

class Cat(Animal):
    def run(self):
        print("Cat is runing...")

class Tortoise(Animal):
    def run(self):
        print("Tortoise is runing slowly...")

def run_twice(animal):
    animal.run()

#run_twice(Cat())
print('type(run_twice()=',type(run_twice(Cat())))

