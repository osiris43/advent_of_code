import time

def compute():
    with open('day2_puzzle_input.txt') as fp:
        input = [x.strip() for x in fp.readlines()]
        horizontal, vertical, aim = 0,0,0
        for movement in input:
            direction, amount = movement.split(' ')

            if direction == 'forward':
                horizontal += int(amount)
                vertical += aim * int(amount)
            
            if direction == 'down':
                aim += int(amount)
            
            if direction == 'up':
                aim -= int(amount)
        
        print(f'answer is {horizontal * vertical}')

if __name__ == "__main__":
    start = time.perf_counter()
    compute()
    end = time.perf_counter()
    print(f"Execution Time : {end- start:0.6f}" )