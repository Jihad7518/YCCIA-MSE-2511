# Complex Number Calculator (Menu Driven)

def get_complex_input(name):
    print(f"\nEnter complex number {name}:")
    real = float(input("  Real part: "))
    imag = float(input("  Imag part: "))
    return complex(real, imag)

def display_menu():
    print("\n===== COMPLEX NUMBER CALCULATOR =====")
    print("1. Add (A + B)")
    print("2. Subtract (A - B)")
    print("3. Multiply (A * B)")
    print("4. Divide (A / B)")
    print("5. Modulus |A| and |B|")
    print("6. Exit")
    return int(input("Choose an option: "))

# Take input once
A = get_complex_input("A")
B = get_complex_input("B")

while True:
    choice = display_menu()

    if choice == 1:
        print("\nResult (A + B):", A + B)

    elif choice == 2:
        print("\nResult (A - B):", A - B)

    elif choice == 3:
        print("\nResult (A * B):", A * B)

    elif choice == 4:
        print("\nResult (A / B):", A / B)

    elif choice == 5:
        print("\n|A| =", abs(A))
        print("|B| =", abs(B))

    elif choice == 6:
        print("\nExiting calculator...")
        break

    else:
        print("Invalid choice! Please try again.")