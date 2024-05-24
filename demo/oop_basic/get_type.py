import types#引入

print('type(123)',type(123))
print('type(\'123\')',type('123'))
print('type(None)',type(None))
print('type(abs)',type(abs))


def fn():
    pass

print(type(fn)==types.FunctionType)

print(type(abs)==types.BuiltinFunctionType)

print(type(lambda x: x)==types.LambdaType)

print(type((x for x in range(10)))==types.GeneratorType)