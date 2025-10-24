# tests/test_calculator.py
from app.calculator import calculator

def test_soma_correta():
    assert soma(2, 3) == 5

def test_soma_zero():
    assert soma(5, 0) == 5