
def run_fizz_buzz():
    # Get the number from the user
    num = int(input("Enter a number: "))

    # Loop through the numbers from 1 to 100
    for i in range(1, num + 1):
        # Check if the number is divisible by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Check if the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz")
        # Check if the number is divisible by 5
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    run_fizz_buzz()