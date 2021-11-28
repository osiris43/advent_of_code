SLOPE_RUN = 3 
SLOPE_RISE = 1 

def check_for_tree(row1, row2, current_col):
    row1_len = len(row1)
    print(f"Row length:{row1_len}")
    if row1_len <= current_col + SLOPE_RUN:
        # moves back to the beginning of the row
        # when row = 4 and col = 2, should = 1 
        # when row = 4 and col = 3, should = 2
        test_column = current_col + SLOPE_RUN - row1_len
    else:
        test_column = current_col + SLOPE_RUN 

    print(f"Test column: {test_column}")
    return (row2[test_column] == "#", test_column)

def count_trees_hit(map_data):
    current_row = 0
    current_col = 0
    tree_count = 0

    print(f"rows in file: {len(map_data)}")
    while current_row + SLOPE_RISE < len(map_data):
        print(f"Current Row: {current_row}\tCurrent Column: {current_col}")
        result = check_for_tree(map_data[current_row].strip(), map_data[current_row+SLOPE_RISE].strip(), current_col)
        if(result[0]):
            print("hit a tree")
            tree_count += 1
        
        current_row += SLOPE_RISE 
        current_col = result[1] 
    
    return tree_count

def compute():
    with open("map.txt") as fp:
        input_data = fp.readlines()
        count = count_trees_hit(input_data)
        print(f'Trees hit: {count}')

if __name__ == '__main__':
    compute()