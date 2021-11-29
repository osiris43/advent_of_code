import pytest
import day4


def test_parsing():
    data = day4.parse_passports("passport_test_data.txt")
    assert 4 == len(data)

def test_create_passport():
    p = day4.Passport({"eyr":"2029"})
    assert p

def test_create_passport_data():
    p = day4.Passport({"eyr":"2029"})
    assert 2029 == p.expiration 

def test_invalid_passport_id():
    p = day4.Passport({"pid":"afeoij"})
    assert not p.is_valid()

def test_invalid_height():
    p = day4.Passport({"hgt":"123"})
    assert not p.is_height_valid()

def test_invalid_height_not_digit():
    p = day4.Passport({"hgt":"abccm"})
    assert not p.is_height_valid()

def test_invalid_hair_color():
    p = day4.Passport({"hcl":"abccm"})
    assert not p.is_hair_color_valid()
    
    p = day4.Passport({"hcl":"#abccm"})
    assert not p.is_hair_color_valid()
    
    p = day4.Passport({"hcl":"#ab3ccm"})
    assert p.is_hair_color_valid()
        
def test_valid_height():
    p = day4.Passport({"hgt":"192cm"})
    assert p.is_height_valid()

def test_invalid_cm_height():
    p = day4.Passport({"hgt":"123cm"})
    assert not p.is_height_valid()

def test_invalid_birth_year():
    p = day4.Passport({"ecl":"gry", "pid":"860033327", \
        "eyr":"2020", "hcl":"#fffffd", "byr":"2004", "iyr":"2017", "cid":"147", "hgt":"183cm"})

    assert not p.is_valid()

def test_invalid_expiration():
    p = day4.Passport({"ecl":"gry", "pid":"860033327", \
        "eyr":"2019", "hcl":"#fffffd", "byr":"2000", "iyr":"2017", "cid":"147", "hgt":"183cm"})

    assert not p.is_valid()


def test_invalid_issue_year():
    p = day4.Passport({"ecl":"gry", "pid":"860033327", \
        "eyr":"2020", "hcl":"#fffffd", "byr":"1920", "iyr":"2009", "cid":"147", "hgt":"183cm"})

    assert not p.is_valid()


def test_creates_default_values():
    p = day4.Passport({})
    assert -1 == p.expiration 

def test_passport_has_validity():
    p = day4.Passport({})
    assert not p.is_valid()

def test_passport_is_valid():
    p = day4.Passport({"ecl":"gry", "pid":"860033327", "eyr":"2020", "hcl":"#fffffd", "byr":"1937", "iyr":"2017", "cid":"147", "hgt":"183cm"})
    assert p.is_valid()

def test_basic_case():
    passports = day4.parse_passports("passport_test_data.txt")
    d = [day4.Passport(p) for p in passports]
    valid = 0
    for p in d:
        print(p)
        if p.is_valid():
            valid += 1

    assert 2 == valid