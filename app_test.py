"""Unit test file for app.py"""
from app import returnBackwardsString

def test_return_backwards_string():
    """Test return backwards simple string"""
    random_string = "This is my test string"
    random_string_reversed = "gnirts tset ym si sihT"
    assert random_string_reversed == returnBackwardsString(random_string)
