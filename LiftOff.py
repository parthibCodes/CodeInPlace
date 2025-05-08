"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""

def main():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()