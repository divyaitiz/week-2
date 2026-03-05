"""
Personal Finance Calculator for employee benefits.
Collects user input, validates it, and generates a financial summary.
"""


def get_valid_string(prompt):
    """Get a non-empty string input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input. Please enter a non-empty value.")


def get_valid_float(prompt, min_value=None, max_value=None):
    """Get a validated float within optional bounds."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value <= min_value:
                print(f"Value must be greater than {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be less than or equal to {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent):
    """Perform all financial calculations."""
    monthly_salary = annual_salary / 12
    tax_amount = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - tax_amount
    rent_ratio = (monthly_rent / net_salary) * 100
    savings_amount = net_salary * (savings_percent / 100)
    disposable_income = net_salary - monthly_rent - savings_amount

    return {
        "monthly_salary": monthly_salary,
        "tax_amount": tax_amount,
        "net_salary": net_salary,
        "rent_ratio": rent_ratio,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "annual_tax": tax_amount * 12,
        "annual_savings": savings_amount * 12,
        "annual_rent": monthly_rent * 12,
    }


def format_currency(amount):
    """Format number into Indian currency style."""
    return f"₹ {amount:,.2f}"


def print_report(name, annual_salary, tax_percent, monthly_rent, savings_percent, data):
    """Print formatted financial report."""
    print("═" * 44)
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("═" * 44)

    print(f"Employee           : {name}")
    print(f"Annual Salary      : {format_currency(annual_salary)}")
    print("─" * 44)

    print("Monthly Breakdown:")
    print(f"Gross Salary       : {format_currency(data['monthly_salary'])}")
    print(f"Tax ({tax_percent}%)       : {format_currency(data['tax_amount'])}")
    print(f"Net Salary         : {format_currency(data['net_salary'])}")
    print(
        f"Rent               : {format_currency(monthly_rent)} "
        f"({data['rent_ratio']:.1f}% of net)"
    )
    print(
        f"Savings ({savings_percent}%) : " f"{format_currency(data['savings_amount'])}"
    )
    print(f"Disposable         : " f"{format_currency(data['disposable_income'])}")

    print("─" * 44)
    print("Annual Projection:")
    print(f"Total Tax          : {format_currency(data['annual_tax'])}")
    print(f"Total Savings      : {format_currency(data['annual_savings'])}")
    print(f"Total Rent         : {format_currency(data['annual_rent'])}")
    print("═" * 44)


def main():
    """Main execution function."""
    name = get_valid_string("Enter employee name: ")
    annual_salary = get_valid_float("Enter annual salary: ", min_value=0)
    tax_percent = get_valid_float(
        "Enter tax percentage (0-50): ", min_value=0, max_value=50
    )
    monthly_rent = get_valid_float("Enter monthly rent: ", min_value=0)
    savings_percent = get_valid_float(
        "Enter savings percentage (0-100): ", min_value=0, max_value=100
    )

    data = calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent)

    print_report(name, annual_salary, tax_percent, monthly_rent, savings_percent, data)


if __name__ == "__main__":
    main()
