import cmath
import math

# Part 1: Complex Number Calculator

# Just a small helper function to take complex num input from user
def complex_input(name):
    print(f"\nEnter Complex Number {name}:")
    # user gives real and imaginary separately, easier this way
    real = float(input("  Real part: "))
    imag = float(input("  Imag part: "))
    return complex(real, imag)   # python's built-in complex type

def complex_calculator():
    # taking two complex numbers from user
    A = complex_input("A")
    B = complex_input("B")

    print("\n Complex number calculator")
    print(f"A = {A}")
    print(f"B = {B}")

    # these are all built-in operations, python handles automatically
    print("\nAddition (A + B):", A + B)
    print("Subtraction (A - B):", A - B)
    print("Multiplication (A * B):", A * B)
    print("Division (A / B):", A / B)
    print("Modulus |A|:", abs(A))  # abs() gives magnitude
    print("Modulus |B|:", abs(B))

# Part 2: Complex Vector Converter

def rectangular_to_polar():
    # user gives a + jb form values
    a = float(input("Enter real part (a): "))
    b = float(input("Enter imaginary part (b): "))

    z = complex(a, b)

    # magnitude directly using abs()
    magnitude = abs(z)

    # phase angle using cmath.phase, gives angle in radians
    phase_rad = cmath.phase(z)

    # converting radians to degrees, looks nicer for humans
    phase_deg = math.degrees(phase_rad)

    print("\n Rectangular to Polar ")
    print(f"Complex Number: {z}")
    print(f"Magnitude (r): {magnitude}")
    print(f"Phase (θ radians): {phase_rad}")
    print(f"Phase (θ degrees): {phase_deg}")

def polar_to_rectangular():
    # user gives r and angle
    r = float(input("Enter magnitude (r): "))
    theta_deg = float(input("Enter phase (degrees): "))

    # converting degrees to radians because python uses radians for math funcs
    theta_rad = math.radians(theta_deg)

    # formula: a = r cosθ, b = r sinθ
    a = r * math.cos(theta_rad)
    b = r * math.sin(theta_rad)

    z = complex(a, b)

    print("\n Polar to Rectangular")
    print(f"Real part: {a}")
    print(f"Imag part: {b}")
    print(f"Complex Number: {z}")

# Main menu loop, just runs until user exits
def main():
    while True:
        print("\n Complex Number Tool")
        print("1. Complex Calculator (Add/Sub/Mult/Div/Modulus)")
        print("2. Convert (a + jb) → Magnitude & Phase")
        print("3. Convert Magnitude & Phase → (a + jb)")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            complex_calculator()
        elif choice == "2":
            rectangular_to_polar()
        elif choice == "3":
            polar_to_rectangular()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

main()