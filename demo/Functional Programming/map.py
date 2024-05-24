# Python内建了map()和reduce()函数。

# 如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。

# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

#             f(x) = x * x

#                   │
#                   │
#   ┌───┬───┬───┬───┼───┬───┬───┬───┐
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

# [ 1   2   3   4   5   6   7   8   9 ]

#   │   │   │   │   │   │   │   │   │
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

# [ 1   4   9  16  25  36  49  64  81 ]
#map : 绘制……的地图，在地图上标出，定位，似在图上描绘;详细安排，筹划;把……与……相联系;（为绘制地图而）勘测（地区等）;了解信息，提供信息(尤指其编排或组织方式);〈数〉使变换，映射;〈生〉将（基因）置入染色体的特定序列;〈生〉（基因）被安置
# 现在，我们用Python代码实现：
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
list(r)
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# 你可能会想，不需要map()函数，写一个循环，也可以计算出结果：

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

# 的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？

# 所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))#转为字符串

#只需要一行代码。

#reduce :减少;缩小(尺寸、数量、价格等);(使)蒸发;减轻体重;节食;使还原
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x,y):
    return x+y
reduce(add,[1,3,5,7,9])

#当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

#如果要把序列[1,3,5,7,9]变成整数13579
def fn(x,y):
    return x*10+y
reduce(fn,[1,3,5,7,9])

#等价 fn(fn(fn(fn(1,3),5),7),9)

#这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

reduce(fn, map(char2num, '13579'))

#整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


#还可以用lambda函数进一步简化成：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！


#练习
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name[:1].upper()+name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
#print(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def mul(x,y):
        return x*y
    return reduce(mul,L)


# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    inte,floa = s.split('.')
    inte = reduce(lambda x,y:x*10+y,list(map(int,inte)))
    floa = reduce(lambda x,y:x/10+y,list(map(float,floa[::-1])))/10
    return inte+floa
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')