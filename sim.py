import random
import atexit
import sys

sys.tracebacklimit = 0

curr_count = 1
prev_coin = random.randint(0,1)
max_count = 0
max_count_value = "none"

@atexit.register
def print_streak():
    global curr_count, prev_coin, max_count, max_count_value
    print(f'{max_count} {max_count_value}')

def main():
    global curr_count, prev_coin, max_count, max_count_value
    while True:
        curr_coin = random.randint(0,1)
        if curr_coin == prev_coin:
            curr_count += 1
        else:
            if max_count < curr_count:
                max_count_value = "heads" if prev_coin else "tails"
                max_count = curr_count
                print(f"New max streak {max_count} {max_count_value}")
            curr_count = 1

        prev_coin = curr_coin

if __name__ == '__main__':
    main()
