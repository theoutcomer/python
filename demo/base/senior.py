#加载模块
from collections.abc import Iterable
isinstance('abc',Iterable)
isinstance([1,2,3],Iterable)
isinstance(123,Iterable)

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i,value)
#    pass


#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    min = max = L[0]
    for k,v in enumerate(L):
        min = L[k] if L[k] < min else min 
        max = L[k] if L[k] > max else max 

    return (min,max)

#alist = list(range(-1,19))
alist = [x+x for x in range(-1,12) if x%2==0]
a = findMinAndMax(alist)
#print(a)

[m+n for m in 'ABC' for n in 'XYZ']

L = ['Hello', 'World', 18, 'Apple', None]
L1 = [x.lower() for x in L if isinstance(x,str)]
#print(L1)

#斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n=n+1
    return 'Done'

fib(8)
