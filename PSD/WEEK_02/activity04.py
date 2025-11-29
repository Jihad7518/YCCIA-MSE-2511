# Activity 03 - Fibonacci & Factorial (Class Version)

class MathTools:
    # Method to generate Fibonacci series
    def fibonacci(self, length):
        if length < 0:
            return "invalid"
        elif length == 0:
            return []
        elif length == 1:
            return [0]

        series = [0, 1]
        for i in range(2, length):
            series.append(series[-1] + series[-2])
        return series

    # Method to compute factorial
    def factorial(self, number):
        if number < 0:
            return "undefined"
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

# main problem 
tools = MathTools()   # Create one object

num = int(input("Enter a non-negative integer: "))

# Fibonacci
fib = tools.fibonacci(num)
print(f"\nFibonacci series ({num} terms): {fib}")

# Factorial
fact = tools.factorial(num)
print(f"Factorial of {num}: {fact}")