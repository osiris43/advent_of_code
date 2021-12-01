def compute():
    with open('day1_puzzle_input.txt') as fp:
        input = [int(x) for x in fp.readlines()]
        slice_window = 2 # 0-2 to start
        count = 0

        for i, _ in enumerate(input):
            cur = input[i:slice_window+1]
            comp = input[i+1:slice_window+2]
            if sum(cur) < sum(comp):
                print(f'Index: {i}\tCurrent: {sum(cur)}:\tNext: {sum(comp)}')
                count += 1

            slice_window += 1    
        
        print(f'readings increased {count} times')

if __name__ == "__main__":
    compute()
