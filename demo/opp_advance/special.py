#定制类
#1、__str__
class Student(object):
    def __init__(self,name) -> None:
        self.name = name

    def __str__(self) -> str:#__str__()返回用户看到的字符串
        return 'Student object (name:%s)'% self.name    
    
    __repr__ = __str__ #__repr__()返回程序开发者看到的字符串

#print(Student("Michael"))

#2、__iter__
class Fib(object):
    def __init__(self) -> None:
        self.a,self.b = 0,1 #初始化两个计数器a,b
    
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b #计算下一个值 
        if self.a > 100000 : #退出条件
            raise StopIteration();
        return self.a #返回下一个值



for n in Fib():
    pass
    #print(n)

#Fib()[2] 无法读取list值

#3、__getitem__    

class Fib2(object):
    def __getitem__(self,n):
        if isinstance(n,int):#整数
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a 
        if isinstance(n,slice):#n切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L
    #定义属性 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
    def __getarrt__(self,attr):
        if attr =='score':
            return '99'#返回属性值 return lambda: 25
        
f2 = Fib2()
# print(f2[10])

# print(list(range(100)[5:10]))
# print(f2[5:10])


#4、__getarrt__   
class Chain(object):
    def __init__(self,path='') -> None:
        self._path = path
    
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path, path))
    
    def __str__(self):
        return self._path
    
    __repr__ = __str__

print(Chain().api.user.index)
#print(Chain().api.user('jacky').index)
