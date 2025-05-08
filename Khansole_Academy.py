import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    
    
    output = 0
    while(output < 3):   
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        print(f"What is {num1} + {num2}?")
        ans = int(input("Your answer: "))
        if(ans == (num1+num2)):
            output += 1
            print("Correct!")
        else:
            print("Incorrect.")
            print(f"The expected answer is {num1+num2}")
            output = 0
    print("Congratulations! You mastered addition.")
    
if __name__ == '__main__':
    main()