#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
dir('ABC')
#print(dir('ABC'))

print(len('ABC')=='ABC'.__len__())#等价

class MyObject(object):
    def __init__(self) -> None:
        self.x = 9
    
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj,'x'))#hasattr判断对象是否有X属性
print(hasattr(obj,'y'))
setattr(obj,'y',10)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)
getattr(obj,'z',404)#如果没值，返回一个default默认值 
print(getattr(obj,'z',404))
#print(obj.z)#未设置值，上面不会赋值

if(hasattr(obj,'power')):
    fn = getattr(obj,'power')
    print('obj.power:',fn())
else:
    raise ValueError('Value Error')


def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)#自定义
    else:
        return None

