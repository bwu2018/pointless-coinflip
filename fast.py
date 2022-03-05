from numpy.random import randint
import time

def main():
    start_time = time.time()
    coins = randint(2, size=1000000000)
    print(time.time() - start_time)
    return 0

if __name__ == '__main__':
    main()
