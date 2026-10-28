import pytest
from bank import deposit, withdraw


def test_deposit():
    assert deposit(100, 50) == 150


def test_deposit_negative():
    with pytest.raises(ValueError):
        deposit(100, -10)


def test_withdraw():
    assert withdraw(100, 30) == 70


def test_withdraw_all():
    assert withdraw(100, 100) == 0


def test_withdraw_too_much():
    with pytest.raises(ValueError):
        withdraw(100, 500)