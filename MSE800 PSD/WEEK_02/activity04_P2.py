
# Updated version using OBJECT instead of static methods.

class MathSeries:
    # Constructor: runs when the object is created
    def __init__(self, n):
        self.n = n    # store the number n for use in methods

    # Recursive factorial function
    def factorial_recursive(self, x=None):
        if x is None:       # if no value passed, start with self.n
            x = self.n

        if x < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        if x in (0, 1):     # base case
            return 1

        return x * self.factorial_recursive(x - 1)   # recursive step

    # Recursive Fibonacci (returns the nth number)
    def fibonacci_recursive(self, x=None):
        if x is None:
            x = self.n

        if x < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")

        if x == 0:
            return 0
        if x == 1:
            return 1

        return self.fibonacci_recursive(x - 1) + self.fibonacci_recursive(x - 2)

    # print entire Fibonacci series up to n
    def fibonacci_series(self):
        series = []                          # store full series

        for i in range(self.n):              # generate values 0 to n-1
            series.append(self.fibonacci_recursive(i))

        return series

# main part where we use an object
if __name__ == "__main__":

    n = int(input("Enter a non-negative integer: "))

    # Create an object of the MathSeries class
    calc = MathSeries(n)

    # Print full Fibonacci series
    print(f"\nFibonacci series up to {n}: {calc.fibonacci_series()}")

    # Print factorial of n
    print(f"Factorial of {n}: {calc.factorial_recursive()}")
