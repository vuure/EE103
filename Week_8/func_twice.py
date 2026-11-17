def doTwice(func, x):
    return func(func(x))

print(f'{doTwice(lambda x: x**2, 5):.6f}')