class Calculation:
    def __init__(self, N, act):
        self.N = N
        self.act = act

    # Recursive Fibonacci
    def fibonacci_recursive(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    # Recursive Factorial
    def factorial_recursive(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial_recursive(n - 1)

    # Decide which function to run
    def calculate(self):
        if self.act == 0:
            return self.fibonacci_recursive(self.N)
        elif self.act == 1:
            return self.factorial_recursive(self.N)
        else:
            return "Invalid action"


def main():
    N = int(input("Enter N: ")) 
    act = int(input("Enter 0 for Fibonacci or 1 for Factorial: "))

    if N < 0:
        print("Please enter a non-negative integer.")
        return

    calc = Calculation(N, act)
    result = calc.calculate()

    print(f"Result for N={N}: {result}")


if __name__ == "__main__":
    main()