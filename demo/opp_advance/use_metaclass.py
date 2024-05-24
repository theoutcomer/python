# metaclass是创建类，所以必须从‘type'类型派生
class ListMetaclass(type):
    # 1、当前准备创建的类的对象；
    # 2、类的名字；
    # 3、类继承的父类集合；
    # 4、类的方法集合。
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
    
#指示使用ListMetaclass来定制类

class MyList(list,metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)
L.add(2)
L.add(3)
L.add("END")
print(L)

#总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
#ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
#要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
#ORM框架