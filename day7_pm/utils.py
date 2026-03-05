"""
Utility functions for financial calculations and formatting.
"""

from typing import Dict


def format_inr(amount: float) -> str:
    """
    Format a number into Indian currency format (lakhs/crores).

    Example:
        1200000 -> ₹12,00,000.00
    """
    negative = amount < 0
    amount = abs(amount)

    integer_part = int(amount)
    decimal_part = f"{amount:.2f}".split(".")[1]

    s = str(integer_part)
    if len(s) > 3:
        last3 = s[-3:]
        rest = s[:-3]
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        formatted = ",".join(parts) + "," + last3
    else:
        formatted = s

    result = f"₹{formatted}.{decimal_part}"
    return f"-{result}" if negative else result


def calculate_financials(data: Dict) -> Dict:
    """
    Compute financial metrics for an employee.
    """
    annual_salary = data["salary"]
    tax_rate = data["tax"]
    rent = data["rent"]
    savings_rate = data["savings"]

    monthly_salary = annual_salary / 12
    tax_amount = monthly_salary * (tax_rate / 100)
    net_salary = monthly_salary - tax_amount
    savings_amount = net_salary * (savings_rate / 100)
    disposable_income = net_salary - rent - savings_amount
    rent_ratio = (rent / net_salary) * 100 if net_salary else 0
    disposable_ratio = (disposable_income / net_salary) * 100 if net_salary else 0

    return {
        "monthly_salary": monthly_salary,
        "tax_amount": tax_amount,
        "net_salary": net_salary,
        "rent": rent,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "rent_ratio": rent_ratio,
        "disposable_ratio": disposable_ratio,
    }


def financial_health_score(metrics: Dict, savings_rate: float) -> int:
    """
    Calculate a financial health score (0–100).

    Criteria:
    - Rent ratio (30 pts)
    - Savings rate (40 pts)
    - Disposable income (30 pts)
    """
    score = 0

    # Rent score
    if metrics["rent_ratio"] <= 30:
        score += 30
    elif metrics["rent_ratio"] <= 40:
        score += 20
    else:
        score += 10

    # Savings score
    if savings_rate >= 20:
        score += 40
    elif savings_rate >= 10:
        score += 25
    else:
        score += 10

    # Disposable score
    if metrics["disposable_ratio"] >= 30:
        score += 30
    elif metrics["disposable_ratio"] >= 15:
        score += 20
    else:
        score += 10

    return score