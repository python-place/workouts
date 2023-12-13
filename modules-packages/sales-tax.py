from decimal import Decimal

RATES = {
    'Colorado': 0.5,
    'California': 0.7,
    'NewYork': 0.5,
    'Michigan': 0.4
}


def time_percentage(hour):
    return hour / 24


def calculate_tax(amount, state, hour):
    return amount + (amount * RATES[state] * time_percentage(hour))


print(calculate_tax(500, 'Harpo', 12))
