# Activity 03 - Part 1: Fibonacci & Factorial (Robust, Modular Version)
print("Activity 03 - Part 1: Math - Fibonacci & Factorial")

def generate_fibonacci(length):
    if length < 0:
        return "invalid"  # Negative length is invalid
    elif length == 0:
        return []         # Zero-length series is empty
    elif length == 1:
        return [0]        # Series of length 1
    else:
        fib_series = [0, 1]  # Start with first two Fibonacci numbers
        for n in range(2, length):
            next_term = fib_series[n-1] + fib_series[n-2]
            fib_series.append(next_term)
        return fib_series

def compute_factorial(number):
    if number < 0:
        return "undefined"  # Factorial undefined for negative numbers
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

def main():
    """
    Main function to take user input and display Fibonacci series and factorial.
    """
    number = int(input("Enter a non-negative integer: "))
    
    # Generate Fibonacci series
    fib_result = generate_fibonacci(number)
    if fib_result == "invalid":
        print("Error: Fibonacci series length cannot be negative.")
    else:
        print(f"The Fibonacci series with length {number} is: {fib_result}")
    
    # Compute factorial
    fact_result = compute_factorial(number)
    if fact_result == "undefined":
        print("Error: Factorial is undefined for negative numbers.")
    else:
        print(f"The factorial of {number} is: {fact_result}")

# Ensure the program runs only if executed directly
if __name__ == "__main__":
    main()
    
