import random

def main():
    userInput = int(input("How many sides does your dice have?"))
    roll = random.randint(1,userInput)
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()