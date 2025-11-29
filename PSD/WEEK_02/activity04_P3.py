class MathSeries:
    # Using self to refer to the instance

    def factorial_recursive(self, n):
        """
        Calculate factorial of n using recursion.
        self is required because this is an instance method.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * self.factorial_recursive(n - 1)

    def fibonacci_recursive(self, n):
        """
        Calculate nth Fibonacci number using recursion.
        self is used to call other methods of the same object.
        """
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def fibonacci_series(self, n):
        """
        Generate a Fibonacci series from 0 to n.
        Uses self to call fibonacci_recursive.
        """
        series = []
        for i in range(n + 1):
            series.append(self.fibonacci_recursive(i))
        return series


if __name__ == "__main__":
    n = 5

    # Create an instance of the class
    obj1 = MathSeries()

    # Call methods using the instance
    print("Factorial (recursive):", obj1.factorial_recursive(n))
    print("Fibonacci (recursive):", obj1.fibonacci_recursive(n))
    print(f"Fibonacci series (0 to {n}):", obj1.fibonacci_series(n))