#orm 框架 https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072
'Simple ORM usring metaclass'

from typing import Any

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=="Model":
            return type.__new__(cls,name,bases,attrs)
        print('Fuond model:%s' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s==>%s' % (k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings #保存属性和列的映射关系
        attrs['__table__'] = name #假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s' " % key)
        
    def __setattr__(self, key, value):
        self[key] = value
    
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL: %s' %sql)
        print('ARGS: %s' %str(args))

class Field(object):
    def __init__(self,name,column_type) -> None:
        self.name = name
        self.column_type = column_type
    
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):    
    def __init__(self, name) -> None:
        super(StringField,self).__init__(name,'varchar(100)')
    
class IntegerField(Field):
    def __init__(self, name) -> None:
        super(IntegerField,self).__init__(name, 'bigint')

#编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：
class User(Model):
    #定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')

u = User(id=100001,name='Michael',email='michael@21jingji.com',password='My-password123')
u.save()#存库