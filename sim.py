import random
import atexit
import sys

sys.tracebacklimit = 0

curr_count = 1
prev_coin = random.randint(0,1)

@atexit.register
def print_streak():
    global curr_count, prev_coin
    if prev_coin == 0:
        print(f'{curr_count} heads')
    else:
        print(f'{curr_count} tails')

def main():
    global curr_count, prev_coin
    while True:
        curr_coin = random.randint(0,1)
        if curr_coin == prev_coin:
            curr_count += 1
        else:
            curr_count = 1
        prev_coin = curr_coin

if __name__ == '__main__':
    main()