import pytest
import day5

def test_example():
    seat = day5.Seat("FBFBBFFRLR") 
    print(f'Result: {seat.position}')
    assert seat.position == (44, 5) 
    assert seat.id == 357 

def test_start_with_ceiling():
    seat = day5.Seat("BBFFBBFRLL")
    assert seat.position == (102,4) 
    assert seat.id == 820 

def test_sanity():
    seat = day5.Seat("BBFBBBBLRL")
    assert seat.position == (111,2) 
    assert seat.id == 890
