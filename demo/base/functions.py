#定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
x = my_abs(-5) 
#print(x)

#定义函数，类似占位符
def nop():
    pass

#默认参数值
def enroll(name,gender,age=6,city='Guangzhou'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

#enroll('jack','F')

#nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
#可变参数,关键字参数,命名关键字参数
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def person(name,age,*kw,addr,zipcode):
    print('name:',name,'age:',age,'other:',kw)

extra = {'city':'Guangzhou','job':'Engineer'}
#person('Terrence',30,*extra)

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#汉诺塔 递归算法
def f1(n,a,b,c):
    if n==1:
        print(a,'--->',c)
        return 'end'
    else:
        f1(n-1,a,c,b)
        print(a,'--->',c)
        f1(n-1,b,a,c)

#f1(3,'A','B','C')