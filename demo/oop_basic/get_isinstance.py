
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

class Husky(Dog):
    pass

def run_twice(animal):
    animal.run()

#isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h,Animal))#true
print(isinstance(d,Husky))#false

#还可以判断变量类型
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

#或者变量类型集合中的其中一种
print(isinstance([1,2,3],(list,tuple)))

#优先使用isinstance