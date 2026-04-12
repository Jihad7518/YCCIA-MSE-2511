# Temperature Converter

# Input must start with 'F' or 'C'.

# Convert Fahrenheit → Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# Convert Celsius → Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

# MAIN PROGRAM

user_input = input("Enter temperature (e.g., F51 or C20): ").strip()

# Input must have at least 2 characters
if len(user_input) < 2:
    print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
else:
    prefix = user_input[0]      # First character: 'F' or 'C'
    number_part = user_input[1:]  # Everything after prefix

    # Validate prefix
    if prefix not in ("F", "C"):
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
    else:
        # Validate that the remaining part is a number
        if not number_part.isdigit():
            print("Invalid input. Temperature must be a number after the prefix.")
        else:
            temp_value = float(number_part)

            # Fahrenheit → Celsius
            if prefix == "F":
                converted = fahrenheit_to_celsius(temp_value)
                print(f"F{temp_value:.0f} degrees Fahrenheit is converted to {converted:.2f} degrees Celsius")

            # Celsius → Fahrenheit
            elif prefix == "C":
                converted = celsius_to_fahrenheit(temp_value)
                print(f"C{temp_value:.0f} degrees Celsius is converted to {converted:.2f} degrees Fahrenheit")


# Temperature Converter (Class Version)

class TemperatureConverter:

    # Constructor to store user input
    def __init__(self, temp_input):
        self.temp_input = temp_input.strip()

    # Convert Fahrenheit -> Celsius
    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

    # Convert Celsius -> Fahrenheit
    def celsius_to_fahrenheit(self, c):
        return (c * 9 / 5) + 32

    # Main method to interpret and convert
    def convert(self):
        # Input must be at least 2 characters
        if len(self.temp_input) < 2:
            return "Invalid input. Please enter using prefix 'C' or 'F'."

        prefix = self.temp_input[0]         # First character
        number_part = self.temp_input[1:]   # Remaining characters

        # Validate prefix
        if prefix not in ("C", "F"):
            return "Invalid input. Please enter using prefix 'C' or 'F'."

        # Validate number part
        if not number_part.isdigit():
            return "Invalid input. Temperature must be a number after the prefix."

        value = float(number_part)  # Convert to number

        # If input starts with Fahrenheit → convert to Celsius
        if prefix == "F":
            converted = self.fahrenheit_to_celsius(value)
            return f"F{value:.0f} degrees Fahrenheit is converted to {converted:.2f} degrees Celsius"

        # If input starts with Celsius → convert to Fahrenheit
        else:
            converted = self.celsius_to_fahrenheit(value)
            return f"C{value:.0f} degrees Celsius is converted to {converted:.2f} degrees Fahrenheit"


if __name__ == "__main__":
    user_input = input("Enter temperature (e.g., F51 or C20): ")

    converter = TemperatureConverter(user_input)
    print(converter.convert())
