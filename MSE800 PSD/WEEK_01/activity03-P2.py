# Activity 03 - Part 2: Fibonacci & Factorial (Using math module)
import math  # For factorial function

def generate_fibonacci(length):
    if length < 0:
        return "invalid"  # Negative length is invalid
    elif length == 0:
        return []         # Empty series
    elif length == 1:
        return [0]        # Series with only 0
    else:
        fib_series = [0, 1]  # Start with first two Fibonacci numbers
        for n in range(2, length):
            next_term = fib_series[n-1] + fib_series[n-2]
            fib_series.append(next_term)
        return fib_series

def compute_factorial(number):
    if number < 0:
        return "undefined"  # Factorial undefined for negatives
    return math.factorial(number)  # Built-in factorial

def main():
    """
    Main function to take user input and display results.
    """
    number = int(input("Enter a non-negative integer: "))
    
    # Generate Fibonacci series
    fib_result = generate_fibonacci(number)
    if fib_result == "invalid":
        print("Error: Fibonacci series length cannot be negative.")
    else:
        print(f"Fibonacci series with length {number}: {fib_result}")
    
    # Compute factorial
    fact_result = compute_factorial(number)
    if fact_result == "undefined":
        print("Error: Factorial is undefined for negative numbers.")
    else:
        print(f"Factorial of {number} = {fact_result}")

# Ensure the program runs only if executed directly
if __name__ == "__main__":
    main()