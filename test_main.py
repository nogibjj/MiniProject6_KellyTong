#this is for testing functions in main.py

from main import subtraction

def test_subtraction():
    "testing the subtraction function in main.py"
    assert subtraction(5,5) == 0
    assert subtraction (1,6) == -5
    assert subtraction (6,1) == 5