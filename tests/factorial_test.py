import pytest
from excercises import factorial

def test_factorial_normalNum():
    assert factorial.fact(5)==120
    assert factorial.fact(2)==2


def test_factorial_negativeNum():
    assert factorial.fact(0)==1

