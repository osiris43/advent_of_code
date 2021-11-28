import pytest
import day2

def test_check_password():
    is_valid = day2.test_password("apple", 1, 3, "a")
    assert is_valid

def test_check_part_two_password():
    is_valid = day2.test_password_2("g", 0, 4, "g")
    assert is_valid
    
    is_valid = day2.test_password_2("aaaag", 0, 4, "g")
    assert is_valid
    
    is_valid = day2.test_password_2("gaaag", 0, 4, "g")
    assert not is_valid