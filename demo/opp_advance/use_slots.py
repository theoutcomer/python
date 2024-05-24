#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class Student(object):
    #pass
    __slots__ = ('name','age')# 1、用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Michael'
s.age = 19

try:
    s.score = 98
except AttributeError as e:
    print("AttributeError:",e)

def set_score(self,score):
    self.score = score

# from types import MethodType
# s.set_score = MethodType(set_score,s)#给实例绑定一个方法（__slots__下不允许）
# s.set_score(60)
# print(s.score)

g = GraduateStudent()
g.score = 99#子类不受限制
# print(g.score)

print(dir(s))