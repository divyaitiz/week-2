"""
Personal Finance Calculator with comparison and scoring.
"""

from typing import Dict
from utils import calculate_financials, format_inr, financial_health_score


def get_employee_data(emp_num: int) -> Dict:
    """
    Collect and validate employee input data.
    """
    print(f"\nEnter details for Employee {emp_num}")

    name = input("Name: ").strip()

    while True:
        try:
            salary = float(input("Annual Salary: "))
            if salary <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid salary. Must be > 0.")

    while True:
        try:
            tax = float(input("Tax % (0-50): "))
            if not 0 <= tax <= 50:
                raise ValueError
            break
        except ValueError:
            print("Invalid tax. Must be 0–50.")

    while True:
        try:
            rent = float(input("Monthly Rent: "))
            if rent <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid rent. Must be > 0.")

    while True:
        try:
            savings = float(input("Savings % (0-100): "))
            if not 0 <= savings <= 100:
                raise ValueError
            break
        except ValueError:
            print("Invalid savings. Must be 0–100.")

    return {
        "name": name,
        "salary": salary,
        "tax": tax,
        "rent": rent,
        "savings": savings,
    }


def display_comparison(emp1: Dict, emp2: Dict) -> None:
    """
    Display side-by-side comparison of two employees.
    """
    print("\n" + "=" * 60)
    print("EMPLOYEE COMPARISON")
    print("=" * 60)

    headers = ["Metric", emp1["name"], emp2["name"]]

    print(f"{headers[0]:<20}{headers[1]:>20}{headers[2]:>20}")
    print("-" * 60)

    rows = [
        ("Monthly Salary", emp1["monthly_salary"], emp2["monthly_salary"]),
        ("Net Salary", emp1["net_salary"], emp2["net_salary"]),
        ("Rent", emp1["rent"], emp2["rent"]),
        ("Savings", emp1["savings_amount"], emp2["savings_amount"]),
        ("Disposable", emp1["disposable_income"], emp2["disposable_income"]),
        ("Health Score", emp1["score"], emp2["score"]),
    ]

    for label, v1, v2 in rows:
        if label == "Health Score":
            print(f"{label:<20}{v1:>20}{v2:>20}")
        else:
            print(
                f"{label:<20}{format_inr(v1):>20}{format_inr(v2):>20}"
            )

    print("=" * 60)


def main() -> None:
    """
    Main program execution.
    """
    emp1_data = get_employee_data(1)
    emp2_data = get_employee_data(2)

    emp1_metrics = calculate_financials(emp1_data)
    emp2_metrics = calculate_financials(emp2_data)

    emp1_score = financial_health_score(
        emp1_metrics, emp1_data["savings"]
    )
    emp2_score = financial_health_score(
        emp2_metrics, emp2_data["savings"]
    )

    emp1_metrics.update({"name": emp1_data["name"], "score": emp1_score})
    emp2_metrics.update({"name": emp2_data["name"], "score": emp2_score})

    display_comparison(emp1_metrics, emp2_metrics)


if __name__ == "__main__":
    main()