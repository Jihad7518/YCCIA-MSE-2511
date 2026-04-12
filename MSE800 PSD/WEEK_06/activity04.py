from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)

print(factorial(5))




fibonacci = lambda n: [0, 1] if n == 2 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2]]

print(fibonacci(10))
