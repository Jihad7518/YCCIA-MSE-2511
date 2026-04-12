from datetime import datetime


def retry():
    return input("Try again? (y/n): ").lower() == "y"


def safe_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("❌ Invalid number.")
        if not retry():
            return None
def safe_int(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("❌ Input cannot be empty.")
            continue
        if value.isdigit():
            return int(value)
        print("❌ Please enter a valid number.")


def safe_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid number format.")
            if not retry():
                return None


def safe_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            print("❌ Invalid date format. Use DD-MM-YYYY.")
            if not retry():
                return None