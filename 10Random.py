import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    number = 0
    while number < N_NUMBERS:
        print(random.randint(1,100))
        number+=1

if __name__ == '__main__':
    main()