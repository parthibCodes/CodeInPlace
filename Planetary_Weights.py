"""
Planetary Weight Calculator

Prompts the user for a weight on Earth and a planet name,
then calculates and prints the equivalent weight on that planet.
"""

def main():
    weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet == "Mercury":
        result = weight * (37.6 / 100)
    elif planet == "Venus":
        result = weight * (88.9 / 100)
    elif planet == "Mars":
        result = weight * (37.8 / 100)
    elif planet == "Jupiter":
        result = weight * (236.0 / 100)
    elif planet == "Saturn":
        result = weight * (108.1 / 100)
    elif planet == "Uranus":
        result = weight * (81.5 / 100)
    elif planet == "Neptune":
        result = weight * (114.0 / 100)

    # Round to 2 decimal places and remove trailing 0s
    formatted_result = str(round(result, 2))
    print(f"The equivalent weight on {planet}: {formatted_result}")

if __name__ == "__main__":
    main()
