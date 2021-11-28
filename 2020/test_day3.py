import pytest
import day3

def test_baby_steps():
    row1 = [".", ".", "#", "."]
    row2 = ["#", ".", "#", "#"]
    current_col_pos = 0 

    result = day3.check_for_tree(row1, row2, current_col_pos)

    assert result[0] 

def test_when_row_is_too_short_move_to_front():
    row1 = [".", ".", "#", "."]
    row2 = [".", "#", ".", "."]
    current_col_pos = 2 

    result = day3.check_for_tree(row1, row2, current_col_pos)

    assert result[0] 

def test_with_strings_instead_of_lists():
    row1 = "..#." 
    row2 = "#.#." 
    current_col_pos = 2 

    result = day3.check_for_tree(row1, row2, current_col_pos)

    assert not result[0] 

def test_full_map():
    with open("test_map.txt") as fp:
        data = fp.readlines()
        tree_count = day3.count_trees_hit(data)

        assert 3 == tree_count

def test_when_column_plus_three_is_row_length():
    row1 = [".", ".", "#", "."]
    row2 = ["#", "#", ".", "."]
    current_col_pos = 1 

    result = day3.check_for_tree(row1, row2, current_col_pos)

    assert result[0] 


