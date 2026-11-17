def estimate_derivative(function, x, h=1e-5):
    derivate = (function(x+h) - function(x-h)) / (2*h)
    return derivate

def take_square(x):
    return x**2

estimated_derivative = estimate_derivative(take_square, 5)
print(f'{estimated_derivative:.6f}')
