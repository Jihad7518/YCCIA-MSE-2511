# Activity 02
# Part 1: Gross Pay

def gross_pay(hours, rate):
    # Multiply hours worked by hourly rate to get gross pay
    return hours * rate


# Part 2: NZ Tax

def nz_tax(annual_income):
    # Select correct income tax rate based on NZ tax brackets
    if annual_income <= 15600:
        tax_rate = 0.105
    elif annual_income <= 53500:
        tax_rate = 0.175
    elif annual_income <= 78100:
        tax_rate = 0.30
    elif annual_income <= 180000:
        tax_rate = 0.33
    else:
        tax_rate = 0.39

    # Calculate how much tax is paid
    tax_amount = annual_income * tax_rate
    return tax_rate, tax_amount


print("\nActivity 02: Gross Pay & NZ Tax\n")

# Take user input
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

# Part 1: Calculate gross pay
gross = gross_pay(hours, rate)
print(f"\nGross Pay: {gross:.2f}")

# Convert weekly income to estimated annual income (simplified assumption)
annual_income = gross * 52
print(f"Annual Income (estimated): {annual_income:.2f}")

# Part 2: Calculate tax and net income
tax_rate, tax_amount = nz_tax(annual_income)
net_income = annual_income - tax_amount

# Print tax results
print(f"\nTax Rate Applied: {tax_rate * 100:.1f}%")
print(f"Tax Amount: {tax_amount:.2f}")
print(f"Net Annual Income: {net_income:.2f}")