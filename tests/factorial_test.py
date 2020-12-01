import pytest
from programs import factorial

def test_factorial_normalNum():
    assert factorial.fact(5)==120

def test_factorial_negativeNum():
    assert factorial.fact(0)==1