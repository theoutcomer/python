from functools import reduce
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def normalize(name):
    return name[0].upper()+name[1:].lower()
    #return name[0].capitalize()

# print(list(map(normalize,['maRila','petER','lLll','lYh'])))
L1 = ['adam','LISA','barT']
L2 = ['maRila','petER','lLll','lYh']

#print(list(map(normalize,L1)))


#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)
L3 = [3, 5, 7, 9]
print('3 * 5 * 7 * 9 =', prod(L3))
if prod(L3) == 945:
    print('测试成功!')
else:
    print('测试失败!')


#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x,y):
    return x * 10 + y#

res = reduce(fn,L3)
print("第二题：list序列变成连后的整数",res)


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = '123.456'

def char2num(s):
    return DIGITS[s]

def str2float(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

L4 = str2float()
print(L4)




# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')    