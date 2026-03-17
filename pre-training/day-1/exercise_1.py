"""
Exercise 1 — Data Types + Operators
Create variables, print a formatted sentence, compute retirement years
and weekly coffee budget.
"""

name = "Hadi"
age = 24
drinks_coffee = True
salary = 75000.00

print(f"My name is {name}, I am {age} years old.")
print(f"Coffee drinker: {drinks_coffee} | Monthly salary: Rs. {salary:,.2f}")

retirement_age = 60
years_until_retirement = retirement_age - age
print(f"\nYears until retirement at {retirement_age}: {years_until_retirement}")

cups_per_day = 3
price_per_cup = 150.0
days_per_week = 7

if drinks_coffee:
    weekly_coffee_budget = cups_per_day * price_per_cup * days_per_week
    print(f"Weekly coffee budget ({cups_per_day} cups/day x Rs. {price_per_cup:.0f}): Rs. {weekly_coffee_budget:,.2f}")
else:
    print("No coffee budget needed — you don't drink coffee!")
