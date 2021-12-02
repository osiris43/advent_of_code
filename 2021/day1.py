import time

def compute():
    with open('day1_puzzle_input.txt') as fp:
        input = [int(x) for x in fp.readlines()]
        slice_window = 2 # 0-2 to start
        count = 0

        for i, _ in enumerate(input):
            cur = sum(input[i:slice_window+1])
            comp = sum(input[i+1:slice_window+2])
            if cur < comp:
                count += 1

            slice_window += 1    
        
        print(f'readings increased {count} times')

if __name__ == "__main__":
    start = time.perf_counter()
    compute()
    end = time.perf_counter()
    print(f"Execution Time : {end- start:0.6f}" )
