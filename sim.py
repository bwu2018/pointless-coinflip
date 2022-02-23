import random
import atexit
import sys
import argparse

parser = argparse.ArgumentParser(description='Simulates coin flips')
parser.add_argument('--quiet','-q', action='store_true', help='Run in quiet mode. Do not print out new max streaks')
parser.add_argument('--total', '-t', action='store_true', help='Print total number of coins flipped.')
parser.add_argument('--count', '-c', action='store_true', help='Print the number of coins flipped since previous highest streak.')

sys.tracebacklimit = 0

curr_count = 1
prev_coin = random.randint(0,1)
max_count = 0
max_count_value = 'none'
total_coins = 1
streak_coins = 1

@atexit.register
def print_streak():
    global curr_count, prev_coin, max_count, max_count_value
    if max_count > 0:
        print(f'{max_count} {max_count_value}')

def main():
    global curr_count, prev_coin, max_count, max_count_value, total_coins, streak_coins
    flags = parser.parse_args()
    while True:
        curr_coin = random.randint(0,1)
        total_coins += 1
        streak_coins += 1
        if curr_coin == prev_coin:
            curr_count += 1
        else:
            if max_count < curr_count:
                max_count_value = 'heads' if prev_coin else 'tails'
                max_count = curr_count
                if not flags.quiet:
                    print(f'New max streak {max_count} {max_count_value}')
                if flags.total:
                    print(f'Total coins flipped {total_coins}')
                if flags.count:
                    print(f'Coins flipped since last streak {streak_coins}')
            curr_count = 1
            streak_coins = 0

        prev_coin = curr_coin

if __name__ == '__main__':
    main()
