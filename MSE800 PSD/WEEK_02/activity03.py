# Recursive Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(n, series=None):
    if series is None:
        series = []
    if len(series) == n:  # Base case: stop when series reaches length n
        return series
    series.append(fibonacci(len(series)))      # Add next Fibonacci number
    return fibonacci_series(n, series)         # Recursive call

# Recursive Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def factorial_series(n, series=None):
    if series is None:
        series = []
    if len(series) == n:  # Base case: stop when series reaches length n
        return series
    series.append(factorial(len(series)))      # Add next factorial
    return factorial_series(n, series)         # Recursive call


n = int(input("Enter the number of terms for Fibonacci and Factorial series: "))

fib_series = fibonacci_series(n)
fact_series = factorial_series(n)

print("Fibonacci series:", fib_series)
print("Factorial series:", fact_series)