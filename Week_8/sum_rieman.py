def riemanSum(func,steps = 1000):
    total_area = 0
    delta_x = 1/steps
    for i in range(steps):
        total_area += func((i+0.5) * delta_x) * delta_x
    return total_area

def funcTwice(x,func):
    return func(func(x))

print(f'{riemanSum(lambda x: x, 1000):.6f}')