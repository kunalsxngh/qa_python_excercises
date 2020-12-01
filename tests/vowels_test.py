import pytest
from excercises import vowels

def test_vowels_allVowels():
    assert vowels.vowels("aeiou")==5

def test_vowels_noVowels():
    assert vowels.vowels("bcdkl")==0
