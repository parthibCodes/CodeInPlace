# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    userInput = int(input("Enter an age in calendar years: "))
    dogYear = DOG_YEARS_MULTIPLIER*userInput
    print(f"That's {dogYear} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()