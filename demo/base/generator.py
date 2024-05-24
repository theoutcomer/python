# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# >>> L = [x * x for x in range(10)]
# >>> L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> g = (x * x for x in range(10))
# >>> g
# <generator object <genexpr> at 0x1022ef630>

# 杨辉三角输出

def yang(max):

    yield [1]

    L = [1, 1]

    while max >= 2:

        yield L #打印并返回 相当于print +return

        max = max - 1

        L = [1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]

for i in yang(10):
    print(i)


# def odd():
#     print('step1')
#     yield 1
#     print('step2')
#     yield 2
#     print('step3')
#     yield 3
# o = odd()
