def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Not enough money")
    return balance - amount