"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    userInput = float(input("Enter a weight on Earth: "))
    mars_weight = userInput * (37.8 / 100)
    print(f"The equivalent weight on Mars: {mars_weight:.2f}")

if __name__ == "__main__":
    main()